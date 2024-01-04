from django.db import models
import pandas as pd 
import os

class Analitic_space(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    

class Dataset(models.Model):
    name = models.CharField(max_length=50)
    size = models.FloatField()
    cant_null = models.IntegerField()
    cant_repeated = models.IntegerField()
    file = models.FileField(upload_to="Datasets/")
    analitic_space = models.ForeignKey(Analitic_space, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    def analyze_dataset(self):
        # Obtener el archivo del dataset
        dataset_file = self.file.path

        if os.path.exists(dataset_file):
            # Cargar el archivo en un DataFrame de Pandas
            df = pd.read_csv(dataset_file)  # Puedes ajustar esto según el formato del archivo

            # Calcular y almacenar el tamaño en MB
            self.size = round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2)

            # Calcular y almacenar la cantidad de filas con valores nulos
            self.cant_null = df.isnull().any(axis=1).sum()

            # Calcular y almacenar la cantidad de filas duplicadas
            self.cant_repeated = df.duplicated().sum()

            # Guardar los cambios en el modelo
            self.save()
        else:
            # Si el archivo no existe, manejar el caso
            pass
    
    # metodos de tratamiento de datos 
