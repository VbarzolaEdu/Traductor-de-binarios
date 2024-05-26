

print("escribir una cantidad de numeros n en Binario,Octal,Decimal y Hexagesimal, indicando como ultimo digito la base del numero, para ser traducidos a los otros sistemas numericos. Para terminar con la introduccion de numeros escriba 'fin'")
print("EJEMPLO: 10102, 12 8, 1010, a 16")


lista=[] #creamos una lista vacia para agregar numeros
while True:
    n=input()
    if n=="fin":
        break
    else:
        lista.append(n)

print("la lista de numeros es: ", lista)



def calculadora(lista):
    for n in lista:
        base = int(n[-1])
        base2 = int(n[-2:])
        num = n[:-1]
        num2= n[:-2]

        if base == 2:
            print("Binario:", num, "Decimal:", int(num,2), "Octal:", oct(int(num,2)), "Hexadecimal:", hex(int(num,2)))
        elif base == 8:
            print("Octal:", num, "Decimal:", int(num, 8), "Binario:", bin(int(num, 8)), "Hexadecimal:", hex(int(num, 8)))
        elif base2 == 10:
            print("Decimal:", num2, "Binario:", bin(int(num2)), "Octal:", oct(int(num2)), "Hexadecimal:", hex(int(num2)))
        elif base2 == 16:
            print("Hexadecimal:", num2, "Decimal:", int(num2, 16), "Binario:", bin(int(num2, 16)), "Octal:", oct(int(num2, 16)))
        else:
            print("Base no válida")


calculadora(lista)



    



        
        

        


        