def constructor_ngrama(n, contenido):
    import re
    texto_limpio = re.sub(r"[\n-]+", " ", contenido)
    puntuacion = r'[.,¿?¡!—\n\r\-]+'
    texto_limpio = re.sub(puntuacion, "", texto_limpio).split()

    n_grama = []
    
    for i in range(len(texto_limpio)):
        palabra = " ".join(texto_limpio[i:i+n])
        n_grama.append(palabra.split())
    return n_grama

def creacion_modelo(n, n_grama):
    modelo = {}
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
            
    return modelo
    
def guardar_datos_json(data):
    import json
    
    with open("data/data.json", "w", encoding="utf-8") as arch:
        json.dump(data, arch, indent=4, ensure_ascii=False)

def ajuste_pesos(modelo):
    for dato in modelo:
        suma_valores = sum(modelo[dato].values()) 
        for dato_secuencia in modelo[dato]:
            modelo[dato][dato_secuencia] /= suma_valores
    return modelo