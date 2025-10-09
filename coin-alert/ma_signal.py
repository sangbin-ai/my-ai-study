from datetime import datetime, timezone
import os

SYMBOL = os.getenv("SYMBOL", "BTC-USD")
INTERVAL = os.getenv("INTERVAL", "1h")

def run_once():
    now = datetime.now(timezone.utc).isoformat()
    print(f"[{now}] Runner OK | SYMBOL={SYMBOL} | INTERVAL={INTERVAL}")

if __name__ == "__main__":
    run_once()
