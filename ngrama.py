from tools.funciones import constructor_ngrama, guardar_datos_json, ajuste_pesos

modelo = {}
n = 2
iteraciones = 0

with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().lower()

n_grama = constructor_ngrama(2, contenido)

if len(n_grama) % 2 == 0:
    iteraciones = len(n_grama)
else:
    iteraciones = len(n_grama) - 1

for i in range(len(n_grama) - 1):
    contexto = n_grama[i][0]
    objetivo = n_grama[i][1]

    if contexto not in modelo:
        modelo[contexto] ={}
             
    if objetivo not in modelo[contexto]:
        modelo[contexto][objetivo] = 1
    else:
        modelo[contexto][objetivo] += 1

model_tuning = ajuste_pesos(modelo)

guardar_datos_json(model_tuning)
