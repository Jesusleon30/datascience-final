# from fastapi import FastAPI, File, UploadFile, HTTPException
# from texto_analyzer.texto_analyzer import TextoAnalyzer

# app = FastAPI()

# # Inicializa el analizador de texto
# analyzer = TextoAnalyzer()

# @app.get("/")
# async def index():
#     return {"message": "🐋 Dockerized FastAPI v1.1"}

# @app.post("/resumen")
# async def obtener_resumen(file: UploadFile = File(...)):
#     try:
#         # Leer el contenido del archivo
#         content = await file.read()

#         # Verificar que el archivo es de tipo texto (UTF-8)
#         try:
#             texto = content.decode('utf-8')  # Decodificar el contenido como texto plano (UTF-8)
#         except UnicodeDecodeError:
#             raise HTTPException(status_code=400, detail="El archivo no es un archivo de texto válido (debe estar en UTF-8).")

#         # Obtener el resumen utilizando el modelo
#         resumen = analyzer.predict_texto(texto)

#         # Retornar el resumen generado
#         return {"resumen": resumen}

#     except Exception as e:
#         # Captura cualquier otro error inesperado
#         raise HTTPException(status_code=500, detail=f"Hubo un error al procesar el archivo: {str(e)}")

# from fastapi import FastAPI, File, UploadFile, HTTPException
# from texto_analyzer.texto_analyzer import TextoAnalyzer
# import os

# app = FastAPI()

# # Inicializa el analizador de texto
# # model_path = " C:\Users\user\Documents\test_datascience\package\texto_cliente\venv\Lib\site-packages\texto_analyzer\model"
# model_path = "C:/Users/user/Documents/test_datascience/package/texto_cliente/venv/Lib/site-packages/texto_analyzer/model"
# analyzer = TextoAnalyzer(model_path=model_path)

# @app.get("/")
# async def index():
#     return {"message": "🐋 Dockerized FastAPI v1.1"}

# @app.post("/resumen")
# async def obtener_resumen(file: UploadFile = File(...)):
#     try:
#         # Leer el contenido del archivo
#         content = await file.read()

#         # Verificar que el archivo es de tipo texto (UTF-8)
#         try:
#             texto = content.decode('utf-8')  # Decodificar el contenido como texto plano (UTF-8)
#         except UnicodeDecodeError:
#             raise HTTPException(status_code=400, detail="El archivo no es un archivo de texto válido (debe estar en UTF-8).")

#         # Obtener el resumen utilizando el modelo
#         resumen = analyzer.predict_texto(texto)

#         # Retornar el resumen generado
#         return {"resumen": resumen}

#     except Exception as e:
#         # Captura cualquier otro error inesperado
#         raise HTTPException(status_code=500, detail=f"Hubo un error al procesar el archivo: {str(e)}")

# from fastapi import FastAPI, File, UploadFile, HTTPException
# from texto_analyzer.texto_analyzer import TextoAnalyzer

# app = FastAPI()

# # Define la ruta de tu modelo aquí
# # Cambia esto por la ruta correcta
# model_path = "C:/Users/user/Documents/test_datascience/package/texto_cliente/venv/Lib/site-packages/texto_analyzer/model"


# # Inicializa el analizador de texto con el modelo
# analyzer = TextoAnalyzer(model_path=model_path)


# @app.get("/")
# async def index():
#     return {"message": "🐋 Dockerized FastAPI v1.1"}


# @app.post("/resumen")
# async def obtener_resumen(file: UploadFile = File(...)):
#     try:
#         # Leer el contenido del archivo
#         content = await file.read()

#         # Verificar que el archivo es de tipo texto (UTF-8)
#         try:
#             # Decodificar el contenido como texto plano (UTF-8)
#             texto = content.decode('utf-8')
#         except UnicodeDecodeError:
#             raise HTTPException(
#                 status_code=400, detail="El archivo no es un archivo de texto válido (debe estar en UTF-8).")

#         # Obtener el resumen utilizando el modelo
#         resumen = analyzer.predict_texto(texto)

#         # Retornar el resumen generado
#         return {"resumen": resumen}

#     except Exception as e:
#         # Captura cualquier otro error inesperado
#         raise HTTPException(
#             status_code=500, detail=f"Hubo un error al procesar el archivo: {str(e)}")

# from fastapi import FastAPI, File, UploadFile, HTTPException
# from texto_analyzer.texto_analyzer import TextoAnalyzer

# app = FastAPI()

# # Ruta del modelo (asegúrate de que sea correcta)
# model_path = "C:/Users/user/Documents/test_datascience/package/texto_cliente/venv/Lib/site-packages/texto_analyzer/model"
# print("Ruta del modelo:", model_path)

# # Inicializa el analizador de texto con el modelo
# analyzer = TextoAnalyzer(model_path=model_path)

# @app.get("/")
# async def index():
#     return {"message": "API en funcionamiento"}

# @app.post("/resumen")
# async def obtener_resumen(file: UploadFile = File(...)):  # Asegúrate de que esté `File(...)` aquí
#     try:
#         # Leer el contenido del archivo
#         content = await file.read()

#         # Verificar que el archivo es de tipo texto (UTF-8)
#         try:
#             texto = content.decode('utf-8')  # Decodificar el contenido como texto plano (UTF-8)
#         except UnicodeDecodeError:
#             raise HTTPException(status_code=400, detail="El archivo no es un archivo de texto válido (debe estar en UTF-8).")
        
#         # Obtener el resumen utilizando el modelo
#         resumen = analyzer.predict_texto(texto)

#         # Retornar el resumen generado
#         return {"resumen": resumen}

#     except Exception as e:
#         # Captura cualquier otro error inesperado
#         raise HTTPException(status_code=500, detail=f"Hubo un error al procesar el archivo: {str(e)}")

from fastapi import FastAPI, File, UploadFile, HTTPException
from texto_analyzer.texto_analyzer import TextoAnalyzer
import os

# Inicializa el analizador de texto con la ruta del modelo
model_path = os.getenv('MODEL_PATH', "C:/Users/user/Documents/test_datascience/package/texto_cliente/venv/Lib/site-packages/texto_analyzer/model")  # Usar variable de entorno o ruta predeterminada
analyzer = TextoAnalyzer(model_path=model_path)

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "🐋 Dockerized FastAPI v1.1"}

@app.post("/resumen")
async def obtener_resumen(file: UploadFile = File(...)):
    try:
        # Leer el contenido del archivo
        content = await file.read()

        # Verificar que el archivo es de tipo texto (UTF-8)
        try:
            texto = content.decode('utf-8')  # Decodificar el contenido como texto plano (UTF-8)
        except UnicodeDecodeError:
            raise HTTPException(status_code=400, detail="El archivo no es un archivo de texto válido (debe estar en UTF-8).")

        # Obtener el resumen utilizando el modelo
        resumen = analyzer.predict_texto(texto)

        # Retornar el resumen generado
        return {"resumen": resumen}

    except Exception as e:
        # Captura cualquier otro error inesperado
        raise HTTPException(status_code=500, detail=f"Hubo un error al procesar el archivo: {str(e)}")
