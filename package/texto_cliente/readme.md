# Setup

Para crear el entorno virtual e instalar los requerimientos:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
``` 

creamos nuestra carpeta libs y dentro de ahy ponemos nuestro lo que avia dentro
de dist:
texto_analyzer-1.0.0-py3-none-any.whl 
texto_analyzer-1.0.0.tar.gz

Para instalarlo, copiar el contenido de `./dist` a `./libs` en otro proyecto:
   ```shell
   pip install .\libs\texto_analyzer-1.0.0-py3-none-any.whl
   ```


una vez hecho nuestro provamos nuestro codigo

python test.py

asi hemos empaqueta nuestro modelo
