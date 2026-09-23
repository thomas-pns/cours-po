import polynome 

p0 = polynome.polynome(1,4,3)
p1 = polynome.polynome(5,2,1)

print("p0 =", p0.show())
print("p1 =", p1.show())

print("Coefficients de p0 :")
print("a =", p0.get_a())
print("b =", p0.get_b())
print("c =", p0.get_c())

print("p0(3) =", p0.evaluation(3))
print("Racines de p0 :", p0.racines())

p_addition = p0.add(p1)
print("p0 + p1 =", p_addition.show())

p_soustraction = p0.subtract(p1)
print("p0 - p1 =", p_soustraction.show())

p_multiplication = p1.multiply(5)
print("5 * p1 =", p_multiplication.show())

