base = int(input("ingrese la base del rectangulo: "))
altura =int(input("ingrese la altura del rectangulo: ")) 
perimetro = 2 * (base + altura) # calcular perimetro en una variable 
area = base * altura # calcular area en una variable 
def calcular_area(base,altura): 
    return base * altura

def calcular_perimetro(base , altura):
    resultado = 2 * (base + altura)
    return resultado

print("esto es el area de un rectangulo:",calcular_area(2,2))
print("esto es el perimetro de un rectangulo: ", calcular_perimetro(2,3))



