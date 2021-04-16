
def area_circum():
    radius = float(input("원의 반지름을 입력하세요 : "))
    area = radius * radius * 3.14 
    circum = 2 * radius * 3.14
    return area, circum

print(area_circum())



