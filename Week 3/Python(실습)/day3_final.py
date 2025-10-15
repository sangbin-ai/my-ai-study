import csv
from datetime import date
from typing import List, Dict

class DateFormatError(Exception):
    pass
def read_scores_csv(path: str) -> List[Dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows=[]
            for i, row in enumerate(reader, start=2):
                name = row.get("name")
            score_str = row.get("score")
            if name is None or score_str is None:
                raise DateFormatError(f"{i}행: 'name' 또는 'score' 열이 없습니다.")
            try:
                score = int(score_str)
            except ValueError:
                raise DateFormatError(f"{i}행: score가 정수가 아닙니다 -> {score_str!r}")
            if not (0 <= score <= 100):
                raise DateFormatError(f"{i}행: 점수 범위(0~100) 벗어남 -> {score}")
            rows.append({"name": name, "score": score})
        if not rows:
            raise DateFormatError("데이터가 비어 있습니다.")
        return rows
    except FileNotFoundError as e:
        # 파일이 없으면 그 사실을 호출자에게 알림
        raise FileNotFoundError(f"CSV 파일을 찾을 수 없습니다: {path}") from e

def summarize(rows: List[Dict]) -> Dict:
    scores = [r["score"] for r in rows]
    total = sum(scores)
    avg = round(total / len(scores), 2)
    return {"count": len(scores), "total": total, "avg": avg, "min": min(scores), "max": max(scores)}

def format_line(rows: List[Dict]) -> str:
    return " | ".join(f'{r["name"]}({r["score"]})' for r in rows)

def main():
    print("🗓 오늘:", date.today())
    path = "scores_basic.csv"   # 어제 만든 파일 그대로 사용 (없으면 예외 발생)

    try:
        rows = read_scores_csv(path)           # 여기서 FileNotFoundError 또는 DataFormatError가 날 수 있음
        info = summarize(rows)
        print("📊 요약:", info)
        print("🧾 한 줄:", format_line(rows))

    except FileNotFoundError as e:
        print("❌ 파일 없음:", e)

    except DateFormatError as e:
        print("❌ 데이터 형식 오류:", e)

    except Exception as e:
        # 예기치 못한 모든 오류 안전망
        print("⚠️ 알 수 없는 오류:", type(e).__name__, e)

    finally:
        print("✅ 종료 정리 실행(파일 닫힘 등)")

if __name__ == "__main__":
    main()