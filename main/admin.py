from django.contrib import admin
from .models import Moto

class MotoAdmin(admin.ModelAdmin):
    # Muestra estas columnas en la lista del admin
    list_display = ('modelo', 'anio', 'precio', 'manual')
    # Permite filtrar por año y si es manual o no
    list_filter = ('anio', 'manual')
    # Permite buscar por modelo, descripción y motor
    search_fields = ('modelo', 'descripcion', 'motor')
    # Ordena por año (descendente)
    ordering = ('-anio',)
    
    # Agrupa los campos en secciones en el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('modelo', 'anio', 'descripcion', 'precio', 'imagen')
        }),
        ('Detalles técnicos', {
            'fields': ('motor', 'velocidad', 'manual', 'pasajeros'),
            'classes': ('collapse',),  # Hace colapsable esta sección
        }),
    )

admin.site.register(Moto, MotoAdmin)