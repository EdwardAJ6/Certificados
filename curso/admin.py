from django.contrib import admin

from .models import Curso, Etapa

admin.site.register(Etapa)


class EtapaInline(admin.TabularInline):
    model = Etapa
    extra = 0

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [EtapaInline]

    def etapas(self, obj):
        return ", ".join([e.nombre for e in obj.etapas.all()])

    list_display = ['nombre', 'descripcion', 'fechaInicio', 'fechaFin', 'etapas']
