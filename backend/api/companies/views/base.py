'''
O views.py é o lugar onde você define a lógica que responde a uma requisição HTTP.
Ou seja: as views recebem uma requisição e retornam uma resposta (normalmente HttpResponse, JsonResponse ou uma resposta automática do DRF).

base.py dentro de views/ (ou mesmo solto como um arquivo base.py) não é uma view diretamente associada a uma URL, mas sim uma classe base de apoio para outras views que herdam dela.

'''

from rest_framework.views import APIView

from companies.utils.exceptions import NotFoundEmployee, NotFoundGroup, NotFoundTask, NotFoundTaskStatus
from companies.models import Employee, Enterprise, Task, TaskStatus

from accounts.models import Group

class Base(APIView):
    #Busca a empresa à qual o usuário pertence, seja como dono (Enterprise) ou funcionário (Employee).
    #Retorna o id da empresa correspondente.
    #Isso é útil para garantir que tudo que ele acessa pertence à empresa dele.
    def get_enterprise_id(self, user_id):
        employee = Employee.objects.filter(user_id=user_id).first()
        owner = Enterprise.objects.filter(user_id=user_id).first()

        if employee:
            return employee.enterprise.id

        return owner.id
    #Primeiro, identifica a empresa do usuário com get_enterprise_id.
    #Depois, busca um Employee com o employee_id que pertença à mesma empresa.
    #Se não encontrar, lança a exceção NotFoundEmployee.
    def get_employee(self, employee_id, user_id):
        enterprise_id = self.get_enterprise_id(user_id)

        employee = Employee.objects.filter(id=employee_id, enterprise_id=enterprise_id).first()

        if not employee:
            raise NotFoundEmployee
        
        return employee
    
    #Busca um Group específico por ID e empresa.
    #Se não achar, lança NotFoundGroup.
    def get_group(self, group_id, enterprise_id):
        group = Group.objects.values('name').filter(id=group_id, enterprise_id=enterprise_id).first()

        if not group:
            raise NotFoundGroup
        
        return group
    
    #Busca o status de uma tarefa (TaskStatus) por ID.
    #Se não existir, lança NotFoundTaskStatus.
    def get_status(self, status_id):
        status = TaskStatus.objects.filter(id=status_id).first()

        if not status:
            raise NotFoundTaskStatus
        
        return status
    
    #Busca uma Task com base no ID e na empresa.
    #e não encontrar, lança NotFoundTask.
    def get_task(self, task_id, enterprise_id):
        task = Task.objects.filter(id=task_id, enterprise_id=enterprise_id).first()

        if not task:
            raise NotFoundTask
        
        return task
