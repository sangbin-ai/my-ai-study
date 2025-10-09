import os, requests
import pandas as pd
import yfinance as yf
from ta.trend import SMAIndicator
from datetime import datetime, timezone
import json

SYMBOL   = os.getenv("SYMBOL", "BTC-USD")
INTERVAL = os.getenv("INTERVAL", "1h")
SHORT_WINDOW = int(os.getenv("SHORT_WINDOW", "20"))
LONG_WINDOW  = int(os.getenv("LONG_WINDOW",  "50"))

TELEGRAM_TOKEN   = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def notify(text: str):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})
    else:
        print("[Notify]", text)

STATE_PATH = "state.json"  # 같은 폴더에 저장

def load_state():
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_state(state: dict):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f)

def signal_label(sig):
    if not sig:
        return "none"
    if sig["golden"]:
        return "golden"
    if sig["dead"]:
        return "dead"
    return "none"

def fetch():
    df = yf.download(tickers=SYMBOL, period="60d", interval=INTERVAL, progress=False)
    df = df.reset_index()
    if "Datetime" in df.columns:
        df.rename(columns={"Datetime":"time"}, inplace=True)
    elif "Date" in df.columns:
        df.rename(columns={"Date":"time"}, inplace=True)
    df = df[["time","Open","High","Low","Close","Volume"]]
    df.columns = ["time","open","high","low","close","volume"]
    return df

def compute_signal(df):
    df["sma_s"] = SMAIndicator(close=df["close"], window=SHORT_WINDOW).sma_indicator()
    df["sma_l"] = SMAIndicator(close=df["close"], window=LONG_WINDOW).sma_indicator()
    df = df.dropna().reset_index(drop=True)
    if len(df) < 2: return None
    prev, last = df.iloc[-2], df.iloc[-1]
    golden = (prev.sma_s < prev.sma_l) and (last.sma_s >= last.sma_l)
    dead   = (prev.sma_s > prev.sma_l) and (last.sma_s <= last.sma_l)
    return {"golden": golden, "dead": dead, "time": str(last.time), "price": float(last.close)}

def run_once():
    now = datetime.now(timezone.utc).isoformat()

    # ✅ 테스트 스위치: TELEGRAM_TEST=1이면 무조건 한 번 메시지 전송
    if os.getenv("TELEGRAM_TEST") == "1":
        notify("🔔 텔레그램 테스트: 연결 OK")
        print(f"[{now}] sent test message")
        return

    # 정상 동작: 가격 불러와 신호 계산
    try:
        df = fetch()
        sig = compute_signal(df)
        label = signal_label(sig)

        state = load_state()
        last_label = state.get("last_label")

        if label == "none":
            print(f"[{now}] No signal yet | {SYMBOL} {INTERVAL}")
            # save_state({"last_label": "none", "time": now})  # 원하면 사용
            return

        if label == last_label:
            print(f"[{now}] Skip duplicate: {label}")
            return

        if label == "golden":
            notify(f"🌕 골든크로스: {SYMBOL} {sig['price']:.2f} @ {sig['time']}")
        elif label == "dead":
            notify(f"🌑 데드크로스: {SYMBOL} {sig['price']:.2f} @ {sig['time']}")

        save_state({"last_label": label, "time": now})

    except Exception as e:
        print(f"[{now}] ERROR: {e}")

if __name__ == "__main__":
    run_once()
