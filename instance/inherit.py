class FourCal:
     def __init__(self, first, second): #초기 setting값 
         self.first = first
         self.second = second
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result


class FourCal_div(FourCal) :
     def div(self):
         result = self.first / self.second
         return result
class MoreFourCal(FourCal) :
     def pow(self) :
          result = self.first ** self.second
          return result

div_data = FourCal_div(4,2)
g = div_data.add() #상속받은 부모의 클래스 안의 메소드 사용가능!
print(g)

q = MoreFourCal(4,2)
q.pow()
print(q.pow())

