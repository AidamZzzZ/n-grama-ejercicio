from tools.funciones import constructor_ngrama, guardar_datos_json, ajuste_pesos

modelo = {}
n = int(input("Ingrese el valor N para construir el N-grama: "))

# lector de archivo de texto
with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().lower()

n_grama = constructor_ngrama(4, contenido)
print("Construyendo n-grama")

iteraciones = 0
if len(n_grama) % 2 == 0:
    iteraciones = len(n_grama)
else:
    iteraciones = len(n_grama) - 1

# inicializando modelo con distribuciones de palabras
for i in range(len(n_grama) - 1):
    contexto = " ".join(n_grama[i][0:n-1])
    objetivo = n_grama[i][1]

    if contexto not in modelo:
        modelo[contexto] ={}
             
    if objetivo not in modelo[contexto]:
        modelo[contexto][objetivo] = 1
    else:
        modelo[contexto][objetivo] += 1
        
print("Modelo entrenado")
model_tuning = ajuste_pesos(modelo)
print("Ajustando valores de los pesos del modelo")
guardar_datos_json(model_tuning)
print("Guardando resultados del modelo en un archivo json.")
