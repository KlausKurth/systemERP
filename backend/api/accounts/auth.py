from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password

from accounts.models import User
from companies.models import Enterprise, Employee

class Authentication:
    def signin(self, email=None, password=None) -> User:
        """
        Realiza autenticação básica do usuário pelo email e senha.

        :param email: email do usuário
        :param password: senha em texto plano
        :return: instância do usuário autenticado
        :raises AuthenticationFailed: se email ou senha forem inválidos
        """

        # Define a exceção que será lançada em caso de falha na autenticação
        exception_auth = AuthenticationFailed("Email e/ou senha incorreto(s)")

        # Verifica se existe usuário com o email informado
        user_exists = User.objects.filter(email=email).exists()

        if not user_exists:
            # Se não existe, lança exceção de autenticação falhada
            raise exception_auth
        
        # Busca o usuário com o email informado
        user = User.objects.filter(email=email).first()

        # Verifica se a senha informada bate com a senha hash armazenada
        if not check_password(password, user.password):
            # Senha incorreta: lança exceção
            raise exception_auth
        
        # Tudo certo, retorna o usuário autenticado
        return user
    

    def signup(self, name, email, password, type_account='owner', company_id=None):
        """
        Realiza o cadastro de um novo usuário. Pode ser proprietário ou funcionário.

        :param name: Nome do usuário
        :param email: Email único
        :param password: Senha em texto plano
        :param type_account: 'owner' ou 'employee'
        :param company_id: Obrigatório se type_account for 'employee'
        :return: Usuário criado
        :raises APIException: Erros de validação ou duplicidade
        """
        if not name:
            raise APIException('O nome não deve ser vazio')

        if not email:
            raise APIException('O email não deve ser vazio')

        if not password:
            raise APIException('A senha não deve ser vazia')

        if User.objects.filter(email=email).exists():
            raise APIException("Este email já existe na plataforma")

        if type_account == 'employee' and not company_id:
            raise APIException('O ID da empresa é obrigatório para funcionários')

        password_hashed = make_password(password)

        # Criação do usuário
        created_user = User.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=(type_account == 'owner')
        )

        # Se for proprietário, cria uma empresa automaticamente
        if type_account == 'owner':
            created_enterprise = Enterprise.objects.create(
                name='Nome da empresa',
                user_id=created_user
            )

        # Se for funcionário, associa à empresa fornecida
        if type_account == 'employee':
            Employee.objects.create(
                enterprise_id=company_id,
                user_id=created_user.id
            )

        return created_user