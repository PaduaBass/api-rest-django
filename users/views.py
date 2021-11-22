from rest_framework import viewsets
from users.models import Usuario
from users.serializer import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

