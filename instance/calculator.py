
class Calculator:
    def __init__(self):
        self.result = 0 

    def add(self, num2):
        self.result += num2
        return self.result

cal = Calculator()
data = cal.add(5)
print(data)


# class Calculator:
#     def __init__(self,num=0):
#         self.result = num 

#     def add(self, num2):
#         self.result += num2
#         return self.result

# cal = Calculator(3)
# data = cal.add(5)
# print(data)
