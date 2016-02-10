from django.contrib import admin

from rango.models import Bares, Tapas

class AdminBar(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

class AdminTapas(admin.ModelAdmin):
    list_display = ('nombre', 'nombrebar', 'votos')

admin.site.register(Bares,AdminBar)
admin.site.register(Tapas, AdminTapas)

