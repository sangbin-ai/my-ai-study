transactions = [12000, 3560,5600, -3500, 19900, 4200, 9800]
transactions.append(7500)
transactions.remove(-3500)
transactions.pop(1)
print(transactions)

transaction = [12000, 3500, 5600, -3500, 19900, 4200, 9800]
TOTAL = sum(transaction)

average = TOTAL / len(transaction)#꼭 기억하자 ★★★중요

print("총합", TOTAL)
print("평균", average)