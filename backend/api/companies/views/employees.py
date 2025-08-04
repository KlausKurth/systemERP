from companies.views.base import Base
from companies.utils.permissions import EmployeesPermission, GroupsPermission
from companies.models import Employee, Enterprise
from companies.serializers import EmployeeSerializer, EmployeesSerializer

from accounts.auth import Authentication
from accounts.models import User, User_Groups

from rest_framework.views import Response, status
from rest_framework.exceptions import APIException


#Responsável por listar todos os funcionários da empresa (exceto o dono) e criar um novo funcionário.
class Employees(Base):

    #Define que essa view só permite acesso a usuários com permissão específica, usando a classe de permissão personalizada EmployeesPermission.
    permission_classes = [EmployeesPermission]

    def get(self, request):

        #Busca o enterprise_id do usuário logado.
        enterprise_id = self.get_enterprise_id(request.user.id)

        # Exclui o dono da empresa (owner_id) da listagem.
        owner_id = Enterprise.objects.values('user_id').filter(id=enterprise_id).first()['user_id']

        employees = Employee.objects.filter(enterprise_id=enterprise_id).exclude(user_id=owner_id).all()

        #Serializa os dados de todos os funcionários e retorna a resposta.
        serializer = EmployeesSerializer(employees, many=True)

        return Response({"employees": serializer.data})


    '''
    Atualiza nome, email e grupos do funcionário.

    Garante que o novo e-mail não esteja duplicado.

    Recria os vínculos com os grupos.
    '''   
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        enterprise_id = self.get_enterprise_id(request.user.id)
        signup_user = Authentication.signup(
            self,
            name=name,
            email=email,
            password=password,
            type_account='employee',
            company_id=enterprise_id
        )

        if isinstance(signup_user, User):
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        
        return Response(signup_user, status=status.HTTP_400_BAD_REQUEST)


'''
Responsável por:

    Exibir os detalhes de um funcionário específico (GET)

    Atualizar dados do funcionário (PUT)

    Deletar (demitir) o funcionário (DELETE)

'''
class EmployeeDetail(Base):
    permission_classes = [EmployeesPermission]

    def get(self, request, employee_id):
        employee = self.get_employee(employee_id, request.user.id)

        serializer = EmployeeSerializer(employee)

        return Response(serializer.data)
    
    def put(self, request, employee_id):
        groups = request.data.get('groups')

        employee = self.get_employee(employee_id, request.user.id)

        name = request.data.get('name') or employee.user.name
        email = request.data.get('email') or employee.user.email

        if email != employee.user.email and User.objects.filter(email=email).exists():
            raise APIException("Esse email já está em uso", code="email_already_use")
        
        User.objects.filter(id=employee.user.id).update(
            name=name,
            email=email
        )

        User_Groups.objects.filter(user_id=employee.user.id).delete()

        if groups:
            # 1,2,3,4 -> [1, 2, 3, 4]
            groups = groups.split(',')

            for group_id in groups:
                self.get_group(group_id, employee.enterprise.id)
                User_Groups.objects.create(
                    group_id=group_id,
                    user_id=employee.user.id
                )

        return Response({"success": True})
    
    '''
    Verifica se o funcionário não é o dono da empresa.

    Remove o funcionário e o usuário correspondente.
    '''
    def delete(self, request, employee_id):
        employee = self.get_employee(employee_id, request.user.id)

        check_if_owner = User.objects.filter(id=employee.user.id, is_owner=1).exists()

        if check_if_owner:
            raise APIException('Você não pode demitir o dono da empresa')
        
        employee.delete()
        
        User.objects.filter(id=employee.user.id).delete()

        return Response({"success": True})