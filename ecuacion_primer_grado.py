# Instrucciones de Decisión

##Caso No.7: Resolver una ecuación de Primer Grado


print("-------------------------------------")
print("----------Resolver Ecuación----------")
print("-------------------------------------")


# input
a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))

#processing

if a!=0:
    x=-b/a

    print("-----RESULTADO-----")
    print("El valor de x es: ")
    print(x)

else:
    print("El valor de a no puede ser 0")