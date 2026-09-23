import polynome 

p0 = polynome.polynome(1,4,3)
p1 = polynome.polynome(5,2,1)
s=5

p2=p1.multiply(s)

print(p2.get_a(), p2.get_b(), p2.get_c())

print(p2.show())

# print(p0.evaluation(3))
# print(p0.racines())
