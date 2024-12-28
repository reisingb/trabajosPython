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

""" 
def calcular_perimetro(radio):
    
    return 2 * math.pi * radio


radio = calcular_perimetro(5)
print("esto es el perimetro de circulo : ", radio) """


""" def calcular_area(radio):
    
    return math.pi * radio ** 2


area = calcular_area(5)
print("esto es el area de un circulo: ", area) """

""" def calcular_volumen(radio):
    
    return (4/3) * math.pi * radio ** 3


volumen = calcular_volumen(5)
print("esto es el volumen de un esfera: ", volumen) """

def calcular_hipotenusa(cateto1, cateto2 ):
    
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2) # sqrt calcula la raiz cuadrada


hipotenusa = calcular_hipotenusa(4,5)
print("el resultado de calcular hipotenusa de un triangulo rectangulo es : ",hipotenusa )