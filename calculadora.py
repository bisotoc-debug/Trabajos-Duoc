bucle = 1

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def divivir(a,b):
    return a/b

while bucle != 0:

    
    Num1 = int(input("Ingrese un numero: "))
    Num2 = int(input("Bien ahora inglese otro numero: "))

    print(f"bien ahora trenda que elijir el metodo a usar\nImportante: primero se usa N1 y luego N2.")
    print(f"====MENU======\n1=SUMAR\n2=RESTAR\n3=MULTIPLICAR\n4=DIVIDIR\n5= SALIR DEL PROGRAMA\n")
    metodo = int(input("METODO ==> "))


    try:

       if metodo == 0:
           print("ERROR EL VALOR INGRESADO DEVE SER UN ENTERO POSITIO VUELVA A COMENZAR")
       else:
            if metodo == 1:
              print(F" la suma es {suma(Num1,Num2)}")
            if metodo == 2:
                print(F" la resta es {resta(Num1,Num2)}")
            if metodo == 3:
                print(F" la multiplicaion es {multiplicar(Num1,Num2)}")
            if metodo == 4:
                print(F" la divicion es {divivir(Num1,Num2)}")
            if metodo == 5:
                bucle = 0
           


    except ValueError:
        print(f"el valor ingresado tieen que ser un numero entero positivo")
    
print("FIN DEL PROGRAMA")






    




