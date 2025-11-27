import datetime

multiplos = []
for numero in range(1, 101):
    if numero % 5 == 0:
        multiplos.append(numero)

fecha_ejecucion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Ejecución del contenedor de python")
print(f"Tecnología: Python 3")
print(f"Fecha y hora de ejecución: {fecha_ejecucion}")
print(f"La acción ejecutada fue buscar múltiplos de 5 hasta el 100.")
print(f"Total de múltiplos encontrados: {len(multiplos)}")
print(f"Lista de múltiplos: {multiplos}")