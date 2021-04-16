def root_ex1(a,b,c) :
    a = int(input("1차항의 계수를 입력하세요 :"))
    b = int(input("2차항의 계수를 입력하세요 :"))
    c = int(input("상수항의 계수를 입력하세요 :"))
    x1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)
    # print(x1,x2)
    return x1, x2

# root_ex1(1,4,4)
print(root_ex1(1,2,-8))