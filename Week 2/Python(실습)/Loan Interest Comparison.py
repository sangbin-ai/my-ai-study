def loan_interest(principal, rate, years):
    interest = principal * rate * years
    return interest
    #principal=원금=1억
    #rate=연 이자율=2%, 0.02
    #years=대출 기간(년)
  #예) 1억 대출, 3년 동안 금리 2% vs 6% 비교
principal = 100_000_000
interest_2=loan_interest(principal, 0.02, 3)
interest_6=loan_interest(principal, 0.06, 3)

print(f"금리 2%일 때 3년 총 이자: {interest_2}원")
print(f"금리 6%일 때 3년 총 이자: {interest_6}원")
print(f"차이: {interest_6 - interest_2}원")           # 단리


def compound_interest(principal, rate, years):
    interest_x = principal * rate * years
    return principal * ((1 + rate) ** years) - principal
principal = 100_000_000
interest_2=compound_interest(principal, 0.02, 3)
interest_6=compound_interest(principal, 0.06, 3)

print(f"금리 2%일 때 3년 총 이자: {interest_2}원")
print(f"금리 6%일 때 3년 총 이자: {interest_6}원")
print(f"차이: {interest_6 - interest_2}원")           # 복리
