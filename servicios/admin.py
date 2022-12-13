from django.contrib import admin
from .models import Servicio, DataFrame

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(DataFrame)