def calcular_promedio(notas):
    suma = 0
    contador = 0
    
    for nota in notas:
        suma += nota
        contador += 1
    
    promedio = suma / contador
    
    if promedio >= 60:
        mensaje = "Aprobado"
    else:
        mensaje = "Reprobado"
    
    return promedio, mensaje

notas = [80, 75, 90, 65, 50]
promedio, resultado = calcular_promedio(notas)

print("El promedio es: " + str(promedio))
print("El resultado es: " + resultado)
