# Setup

Para crear el entorno virtual e instalar los requerimientos:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```


# Descarga del modelo

Para utilizar le modelo, es necesario exportar sus archivos y pegarlos en la carpeta `./model`.
El [ejemplo](https://colab.research.google.com/drive/1F2oKyA-Kx5qljHufP5aIiy93-uUQIETj) que se utiliza en el ejercicio.
vemos donde esta :
Guardar el modelo y el tokenizador en el directorio especificado
path = "./model"


# Para empaquetar

En la carpeta `texto_analyzer`:

 Generar los archivos del modelo en colab y colocarlos en una carpeta `./texto_analyzer/texto_analyzer/model`.

 Generar el paquete
   ```shell
   python .\setup.py sdist bdist_wheel
   ```
una vez ejecutado el setup se creera el dist y el build y otras..
lo que nos interesa en lo que esta dentro del dist:

texto_analyzer-1.0.0-py3-none-any.whl 
texto_analyzer-1.0.0.tar.gz


Para instalarlo, copiar el contenido de `./dist` a `./libs` en otro proyecto:
   ```shell
   pip install .\libs\texto_analyzer-1.0.0-py3-none-any.whl
   ```