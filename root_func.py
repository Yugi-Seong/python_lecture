def get_root(a,b,c):
    r1 = (-b +(b**2-4*a*c)**0.5) / (2*a)
    r2 = (+b +(b**2-4*a*c)**0.5) / (2*a)
    return r1, r2 

result1, result2 = get_root(1,2,-8)
print("해는 %d 또는 %d" %(result1,result2))