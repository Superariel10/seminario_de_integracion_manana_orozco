print("condicionales simples")
edad=input("Incluye edad?")
if (int(edad)>=18):
    print("Mayor de edad")

print("condicionales dos caminos")
temperatura=input("Incluye temperatura?")
if (int(temperatura)>=38):
    print("temperatura alta")
else:
    print("temperatura normal")
    
print("condicionales multiples")
nota=input("Incluir nota?")
if (int(nota)>=90):
    print("Excelente")
elif (int(nota)>=80):
    print("Bueno")
elif (int(nota)>=70):
    print("Aprobado")
else:
    print("Reprobado")
    
print("condicionales if anidados")
tiene_reserva=True
dinero=25
plato="pizza"
if (tiene_reserva):
    if(dinero>=20):
        if plato=="pizza":
            print("Tu pizza cuesta $20. Pedido confirmado")
        else: 
            print("Plato disponible")
    else:
        print("Dinero insuficiente")
else:
    print("No tiene reserva")
    
print("condicionales if anidados bono")
es_empleado=True
antiguedad=365
desempeño=9
salario=1500
if (es_empleado):
    if(antiguedad>=365):
        if desempeño >= 8:
            print("Puede optar al bono")
            if salario >= 1000:
                print("bono de $100")
            else:
                print("bono de $200")
        else: 
            print("No puede optar al bono")
    else:
        print("No cumple la antiguedad requerida")
else:
    print("No es un empleado")