a = int(input ("ingrese este nuemero:" ))
b = int(input ( "ingrese otro numero:" ))
 
c = a // b
r = a % b

if a >= b:
    print("no se  puede inprimir la serie")
else:
     while a<= b:
        print(a)
        a +=3
