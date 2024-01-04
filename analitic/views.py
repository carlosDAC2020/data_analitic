from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import pandas as pd 

from .models import Dataset
from read_dataset.basic_data import get_basic_data

def home(request):
    return render(request, 'analitic/home.html')

def create_analiric_space(request):

    if request.method == 'POST' and request.FILES['archivo_csv']:

        archivo_csv = request.FILES['archivo_csv']

        # Crear una instancia de Dataset
        nuevo_dataset = Dataset()
        nuevo_dataset.name = archivo_csv.name  # Utiliza el nombre del archivo como nombre del dataset
        nuevo_dataset.file = archivo_csv

        # Guardar la instancia del dataset en la base de datos
        nuevo_dataset.save()

        # Realizar el análisis y actualizar los campos 'size', 'cant_null' y 'cant_repeated'
        nuevo_dataset.analyze_dataset()  # Asumiendo que has implementado el método analyze_dataset

        #return JsonResponse(get_basic_data(df))
        return HttpResponse("espacio creado")
    else:
        return render(request,"")
        
    