from tools.funciones import constructor_ngrama, guardar_datos_json, ajuste_pesos, creacion_modelo

modelo = {}
n = int(input("Ingrese el valor N para construir el N-grama: "))

# lector de archivo de texto
with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().lower()

n_grama = constructor_ngrama(4, contenido)
print("Construyendo n-grama")
modelo = creacion_modelo(n, n_grama)
print("Modelo entrenado")
model_tuning = ajuste_pesos(modelo)
print("Ajustando valores de los pesos del modelo")
guardar_datos_json(model_tuning)
print("Guardando resultados del modelo en un archivo json.")
