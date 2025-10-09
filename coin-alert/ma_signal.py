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
        if not sig:
            print(f"[{now}] No signal yet | {SYMBOL} {INTERVAL}")
            return
        if sig["golden"]:
            notify(f"🌕 골든크로스: {SYMBOL} {sig['price']:.2f} @ {sig['time']}")
        elif sig["dead"]:
            notify(f"🌑 데드크로스: {SYMBOL} {sig['price']:.2f} @ {sig['time']}")
        else:
            print(f"[{now}] No cross. price={sig['price']:.2f}")
    except Exception as e:
        print(f"[{now}] ERROR: {e}")

if __name__ == "__main__":
    run_once()
