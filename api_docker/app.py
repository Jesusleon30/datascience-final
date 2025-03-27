from fastapi import FastAPI, File, UploadFile, HTTPException
from texto_analyzer.texto_analyzer import TextoAnalyzer
import os

# Inicializa el analizador de texto con la ruta del modelo
model_path = os.getenv('MODEL_PATH', "C:/Users/user/Documents/test_datascience/package/texto_cliente/venv/Lib/site-packages/texto_analyzer/model")  
analyzer = TextoAnalyzer(model_path=model_path)

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "🐋 Dockerized FastAPI v1.1"}

@app.post("/resumen")
async def obtener_resumen(file: UploadFile = File(...)):
    try:
       
        content = await file.read()

        # Verificar que el archivo es de tipo texto (UTF-8)
        try:
            texto = content.decode('utf-8')  # Decodificar el contenido como texto plano (UTF-8)
        except UnicodeDecodeError:
            raise HTTPException(status_code=400, detail="El archivo no es un archivo de texto válido (debe estar en UTF-8).")

        
        resumen = analyzer.predict_texto(texto)

       
        return {"resumen": resumen}

    except Exception as e:
        # Captura cualquier otro error inesperado
        raise HTTPException(status_code=500, detail=f"Hubo un error al procesar el archivo: {str(e)}")
