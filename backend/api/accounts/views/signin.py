from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

# A classe Signin agora herda de APIView e Base
class Signin(Base):
    def post(self, request) -> Response:
        # Obtém o email e a senha do corpo da requisição
        email = request.data.get('email')
        password = request.data.get('password')

        # Realiza autenticação do usuário com base no email e senha
        user = Authentication.signin(self, email=email, password=password)

        # Gera tokens JWT (refresh e access) para o usuário autenticado
        token = RefreshToken.for_user(user)

        # Obtém informações da empresa (permissões e se é proprietário)
        enterprise = self.get_enterprise_user(user.id)

        # Serializa os dados do usuário para envio na resposta
        serializer = UserSerializer(user)

        # Retorna resposta com dados do usuário, informações da empresa e tokens JWT
        return Response({
            "user": serializer.data,
            "enterprise": enterprise,
            "refresh": str(token),                  #  para retornar string do token
            "access_token": str(token.access_token) #  para retornar string do access token
        })

