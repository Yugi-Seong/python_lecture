class Cat :
    #클래스를 구성할때 초기화 해주기
    def __init__(self, name, color ="흰색"): #정해진 식별자 : 내장 변수 : __init__ 사용
        self.a = name
        self.b = color 

    def meow(self,speed) :
        print("내 이름은 {}, 색깔은 {}, 야옹 야옹".format(self.a, self.b))
        print("속도는",speed)

nabi = Cat("나비") 
nabi.meow(100)

nero = Cat("네로","검은색")
nero.meow(300)

mimi = Cat("미미","갈색")
mimi.meow(400)
# self 대신에 다른 변수를 사용해도 상관없음 
                