import os
import torch
from transformers import T5TokenizerFast, T5ForConditionalGeneration


class TextoAnalyzer:
    def __init__(self):
        # Crear la ruta del modelo relativa en el __init__
        # Ruta relativa al directorio actual
        self.model_path = os.path.join(os.path.dirname(__file__), "model")

        
        self.tokenizer = T5TokenizerFast.from_pretrained(self.model_path)
        self.model = T5ForConditionalGeneration.from_pretrained(
            self.model_path)

        # Determinar el dispositivo (GPU si disponible, de lo contrario CPU)
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        # Mover el modelo al dispositivo
        self.model = self.model.to(self.device)

        # Imprimir la ruta del modelo
        print(f"Ruta del modelo: {self.model_path}")

    def predict_texto(self, text):
        # Tokenizar el texto de entrada
        inputs = self.tokenizer(text, return_tensors="pt",
                                truncation=True, padding=True, max_length=512)

        # Obtener los ids de los tokens y la máscara de atención
        input_ids = inputs["input_ids"].to(self.device)
        attention_mask = inputs["attention_mask"].to(self.device)

        # Generar la predicción utilizando el modelo
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=input_ids, attention_mask=attention_mask, max_length=150, num_beams=4, early_stopping=True)

        # Decodificar el texto generado
        resultado = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return resultado



if __name__ == "__main__":
    # Crear una instancia de TextoAnalyzer
    analyzer = TextoAnalyzer()

    # Verificar si el objeto analyzer fue creado correctamente
    if not hasattr(analyzer, 'tokenizer'):
        print("Error: No se pudo cargar el modelo.")
    else:
        
        ARTICLE = """
             ¿Qué es un robot?
             Un robot es una máquina diseñada para llevar a cabo una serie de tareas de manera autónoma o semiautónoma. Dependiendo de su diseño y función, los robots pueden estar equipados con sensores que les permiten interactuar con su entorno, procesadores que interpretan la información que reciben y actuadores que les permiten realizar movimientos físicos.

             Tipos de robots
             Robots industriales: Son los más conocidos y se utilizan principalmente en fábricas y líneas de ensamblaje. Son capaces de realizar tareas repetitivas con gran precisión y velocidad, como la soldadura, el ensamblaje de piezas y la pintura de automóviles.

             Robots de servicio: Estos robots están diseñados para interactuar directamente con personas y ayudar en tareas cotidianas, como los robots aspiradores o asistentes personales. Algunos también se utilizan en atención al cliente, como en restaurantes o comercios.

             Robots médicos: En el campo de la salud, los robots están revolucionando las cirugías y el diagnóstico. Por ejemplo, los robots quirúrgicos permiten realizar procedimientos de alta precisión a través de incisiones mínimas, lo que reduce el tiempo de recuperación de los pacientes.

            Robots de exploración: Utilizados en la exploración espacial, submarina y en zonas de difícil acceso, estos robots pueden operar en condiciones extremas donde los humanos no pueden estar presentes, como en Marte o en las profundidades del océano.

            Impacto en la sociedad
            La llegada de los robots a diferentes sectores plantea importantes desafíos y oportunidades para la sociedad:

             Automatización y empleo: La automatización de ciertas tareas mediante robots puede mejorar la productividad, pero también puede generar preocupación sobre la pérdida de empleos en sectores como la manufactura. Sin embargo, se espera que surjan nuevas oportunidades laborales en áreas relacionadas con la robótica y la inteligencia artificial.
             Mejoras en la calidad de vida: Los robots pueden mejorar la calidad de vida de las personas, especialmente en el ámbito de la salud. Por ejemplo, los robots pueden ayudar a cuidar a los ancianos, realizar diagnósticos médicos más rápidos y precisos, o incluso realizar tareas domésticas.

             Ética y privacidad: A medida que los robots se vuelven más inteligentes y autónomos, surgen preguntas sobre la ética de su uso. ¿Deberían tener derechos? ¿Quién es responsable si un robot causa daño? Además, el uso de robots que recopilan datos de las personas genera preocupaciones sobre la privacidad y el control de la información personal.

             Educación y aprendizaje: Los robots pueden tener un papel clave en la educación, ya que pueden proporcionar experiencias de aprendizaje personalizadas y ayudar a los estudiantes a desarrollar habilidades en ciencia, tecnología, ingeniería y matemáticas (STEM).

            El futuro de los robots
            El futuro de la robótica es prometedor y está lleno de posibilidades. A medida que la inteligencia artificial y los sistemas autónomos continúan avanzando, los robots podrían ser cada vez más inteligentes, capaces de realizar tareas complejas, tomar decisiones por sí mismos y aprender de su entorno.

            Los robots también podrían colaborar con los humanos en lugar de reemplazarlos, lo que llevaría a una mayor interacción entre personas y máquinas. El trabajo conjunto de humanos y robots podría dar lugar a un futuro en el que se amplifiquen nuestras capacidades en lugar de sustituirlas.

            Conclusión
             La robótica está cambiando rápidamente el mundo en que vivimos. Si bien existen desafíos, como la pérdida de empleos y las preocupaciones éticas, los robots tienen el potencial de mejorar significativamente muchos aspectos de la vida humana. La clave estará en cómo los integremos de manera responsable en nuestra sociedad, asegurándonos de que su desarrollo beneficie a todos.
        """ 

       
        resultado = analyzer.predict_texto(ARTICLE)

        
        print("Resultado generado: ")
        print(resultado)

      
        print(f"Ruta del modelo cargado: {analyzer.model_path}")
