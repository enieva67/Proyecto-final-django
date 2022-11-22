from django.shortcuts import render
from .forms import EncuestaForm
from django.views import View

# Create your views here.

def pventa(request):
    return render(request, "afterselling/pventa.html")

class Encuesta(View):
    def get(self,request):
        formulario_encuesta = EncuestaForm()
        return render(request, "afterselling/encuesta.html", {'forms_encuesta': formulario_encuesta})

    def post(self, request):
        formulario_encuesta = EncuestaForm(data=request.POST)
        if formulario_encuesta.is_valid():
            formulario_encuesta.save()

        return render(request, "afterselling/pventa.html")