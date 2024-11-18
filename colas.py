from collections import deque
import time
cola_impresion = deque()
def agregar_trabajo(documento):
    cola_impresion.append(documento)
    print(f"Trabajo '{documento}' añadido a la cola de impresión.")
def procesar_trabajo():
    if cola_impresion:
        documento_procesado = cola_impresion.popleft()
        print(f"Imprimiendo '{documento_procesado}'...")
        time.sleep(2)  # Espera 2 segundos para simular el tiempo de impresión
        print(f"Trabajo '{documento_procesado}' impreso.")
    else:
        print("No hay trabajos en la cola de impresión.")
agregar_trabajo("Informe Anual")
agregar_trabajo("Presentación del Proyecto")
agregar_trabajo("Factura del Cliente")
for _ in range(4):
    procesar_trabajo()
print(f"Trabajos restantes en la cola: {list(cola_impresion)}")  # Salida: []