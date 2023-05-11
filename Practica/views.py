from django.http import HttpResponse
from django.template import Template, Context
from  django.template.loader import get_template
from django.shortcuts import render
def saludo(request):
    nombre = "Mafe"
    apellido= "Velandia"
    doc_externo= get_template('miplantilla.html')
    documento=doc_externo.render({"nombre_persona":nombre,"apellido_persona":apellido})
    return HttpResponse(documento)
def busqueda_productos(request):
    return render(request, "buscar_productos.html")

def buscar(request):
    mensaje="Articulo buscado: ", request.GET["producto"]
    return HttpResponse(mensaje)

def suma(request):
    return render(request, "suma.html")
    
def sumar(request):
    suma = "La suma es : ",int(request.GET["numero1"] )+ int(request.GET["numero2"])
    return HttpResponse(suma)