primeirold= int(input("digite o primeiro lado: "))
segundold= int(input("digite o segundo lado: "))
terceirold= int(input("digite o terceiro lado: "))

if primeirold == segundold == terceirold:
    print("o triangulo e equilatero")
    
elif primeirold == segundold or primeirold == terceirold or segundold == terceirold:
    print("O triangulo e isosceles")
    
else:print("o triangulo e escaleno")