from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from typing import Any, Dict, Optional

from companies.models import Enterprise, Employee
from accounts.models import User_Groups, Group_Permissions

class Base(APIView):
    def get_enterprise_user(self, user_id) -> dict[str, Any] | None:
        # Estrutura padrão da resposta
        enterprise = {
            "is_owner": False,       # Indica se o usuário é dono da empresa
            "permissions": []        # Lista de permissões caso ele seja funcionário
        }

        # Verifica se o usuário é dono de alguma empresa
        enterprise['is_owner'] = Enterprise.objects.filter(user_id=user_id).exists()

        # Se for dono, já retorna as informações
        if enterprise['is_owner']:
            return enterprise

        # Se não é dono, tenta buscar se é funcionário
        employee = Employee.objects.filter(user_id=user_id).first()

        # Se não for funcionário, lança exceção
        if not employee:
            raise APIException("Este usuário não é um funcionário")

        # Busca todos os grupos que o usuário pertence
        groups = User_Groups.objects.filter(user_id=user_id).all()

        for g in groups:
            group = g.group  # Acessa o objeto do grupo relacionado ao User_Groups

            # Aqui estava o erro: `group_id` não está definido no escopo. Devemos usar `group.id`
            permissions = Group_Permissions.objects.filter(group_id=group.id).all()

            for p in permissions:
                # Aqui estava outro erro: `p_permission.name` é uma variável que não existe.
                # O correto é `p.permission.name`
                enterprise['permissions'].append({
                    "id": p.permission.id,
                    "label": p.permission.name,
                    "codename": p.permission.codename
                })

        return enterprise        