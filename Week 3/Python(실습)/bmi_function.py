def bmi(weight, height):
    bmi_value = weight / (height/100)**2
    return round(bmi_value, 2)
print(bmi(70, 170))

def even_numers(lst):
    return [x for x in lst if x % 2 == 0]
print(even_numers([1, 2, 3, 4, 5, 6]))