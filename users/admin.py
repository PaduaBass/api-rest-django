from django.contrib import admin
from users.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'login', 'senha')
    list_display_links = ('nome', 'login')
    search_fields = ('login', 'nome')

admin.site.register(Usuario, Usuarios)
# Register your models here.
