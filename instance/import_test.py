import fourcal_class
from fourcal_class import FourCal as FC #fourcal_class.py 로부터 FourCal 클래스만 불러오길 원할때 

# b = fourcal_class.FourCal(4,2)
# b = FourCal(4,2)
b = FC(4,2)
c = b.add()

print(c)