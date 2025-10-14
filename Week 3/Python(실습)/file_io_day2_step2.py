with open("notes_day2.txt", "w", encoding="utf-8") as f: #"w" 새로 쓰기
    f.write("Day2 파일 입출력 연습 시작! \n")
    f.write("이 파일은 파이썬으로 생성된 텍스트 파일입니다.\n")
with open("notes_day2.txt", "a", encoding="utf-8") as f: # "a" 추가해서 쓰기
    f.write("append 모드로 한 줄 추가!\n")
with open("notes_day2.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("[전체 읽기 결과]\n", content)
with open("notes_day2.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("[줄 단위]", line.strip())

import csv

with open("scores_basic.csv", "w", encoding="utf-8", newline="")as f:
    w= csv.writer(f)
    w.writerow(["이름", "점수"])
    w.writerows([["상빈", 95], ["민수",82], ["지현",77], ["도윤",60]])
with open("scores_basic.csv", "r", encoding="utf-8")as f:
    r=csv.reader(f)
    for row in r:
        print(row)
