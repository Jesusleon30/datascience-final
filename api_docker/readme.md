# Setup

Para crear el entorno virtual e instalar los requerimientos:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```  

creamos nuestro libs y dentro texto_analyzer-1.0.0-py3-none-any.whl 

Para instalarlo, copiar el contenido de `./dist` a `./libs` en otro proyecto:
   ```shell
   pip install .\libs\texto_analyzer-1.0.0-py3-none-any.whl
   ```



configuramos el dockerfile 
y si queremos dinamismo configuramos 
el docker-compose.yaml


creamos una imagen
docker build -t mi-api-fastapi .

Ejecutar el contenedor:
docker run -d -p 8000:8000 mi-api-fastapi



provamos nuestro app.py nos llevara a nuestra web fastapi y ahy podemos provar el codigo 

levantar aplicacion: 

fastapi dev app.py




una vez creada la imagen en el docker lo metemos en run para ver si no ahy errores y 
que todo este bien listo 





