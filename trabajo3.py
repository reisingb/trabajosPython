import math
""" base = int(input("ingrese la base del rectangulo: "))
altura =int(input("ingrese la altura del rectangulo: ")) """ 
""" perimetro = 2 * (base + altura) # calcular perimetro en una variable 
area = base * altura # calcular area en una variable  """
""" def calcular_area(base,altura): 
    return base * altura

def calcular_perimetro(base , altura):
    resultado = 2 * (base + altura)
    return resultado """

""" print("esto es el area de un rectangulo:",calcular_area(2,2))
print("esto es el perimetro de un rectangulo: ", calcular_perimetro(2,3)) """

""" x1= float(input("ingrese el valor de x1: "))
x2= float(input("ingrese el valor de x2: "))
y1= float(input("ingrese el valor de y1: "))
y2= float(input("ingrese el valor de y2: ")) """


""" def calcular_area(x1,x2,y1,y2):
    base= abs(x1 - x2)  # abs asegura que sean positvos los valores 
    altura= abs(y1 - y2)    
    return  base * altura
     
resultado = calcular_area(1,3,4,5)
print("el area del rectangulo es: ", resultado) """

""" radio = int(input("ingrese el perimetro deseado: ")) """

def calcular_perimetro(radio):
    
    return 2 * math.pi * radio


radio = calcular_perimetro(5)
print("esto es el perimetro de un rectangulo: ", radio)