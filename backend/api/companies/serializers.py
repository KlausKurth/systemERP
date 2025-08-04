'''
Um Serializer é como um tradutor entre o mundo Python/Django e o mundo JSON (API).
ModelSerializer: já entende como o model funciona (campos, tipos etc.).
Meta: define qual modelo ele está serializando e quais campos incluir no JSON.
"self" é o serializer atual, e obj é a instância do modelo que está sendo serializada
'''

'''
-> Any Significa: “essa função vai retornar qualquer tipo de valor”.

Outros exemplos:

    -> None → não retorna nada

    -> str → retorna string

    -> dict[str, Any] → retorna dicionário

Isso não muda o comportamento, é só pra documentar o código e ajudar o editor (como VSCode) com sugestões.

'''

from rest_framework import serializers

from companies.models import Employee, Task
from accounts.models import User_Groups, User, Group, Group_Permissions

from django.contrib.auth.models import Permission
from typing import Any


# Mostra apenas id, name e email do funcionário (dados vindos do User).
# Pega o name que está no modelo User relacionado ao Employee.
class EmployeesSerializer (serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email'
        )

    def get_name(self, obj) -> Any:
        return obj.user.name

    def get_email(self, obj) -> Any:
        return obj.user.email


#Igual ao anterior, mas também traz os grupos que o funcionário pertence:
#az um loop para montar os dados dos grupos em formato JSON.
class EmployeeSerializer (serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()    

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email',
            'groups'    
        )

    def get_name(self, obj) -> Any:
        return obj.user.name

    def get_email(self, obj) -> Any:
        return obj.user.email    
    
    def get_groups(self, obj):
        groupsDB = User_Groups.objects.filter(user_id=obj.user.id).all()
        groupsDATA = []

        for group in groupsDB:
            groupsDATA.append({
                'id': group.group.id,
                'name': group.group.name
            })

        return groupsDATA    
    
                    
#Ele traz os grupos com suas permissões.
#Pega as permissões de cada grupo e retorna como lista de dicionários.
class GroupSerializer (serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'permissions'
        )

    def get_permissions(self, obj) -> None:
        groups = Group_Permissions.objects.filter(group_id=obj.id).all()
        permissions = []

        for group in groups:
            permissions.append({
                'id': group.permissions.id,
                'label': group.permission.name,
                'codename': group.permission.codename
            })

        return permissions


class PermissionsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'id',
            'name',
            'codename'
        )


class TasksSerializer (serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model =  Task
        fields = (
            'id',
            'title',
            'description',
            'due_date',
            'created_at',
            'status'
        )

    def get_status(self, obj) -> Any:
        return obj.status.name


class TaskSerializer (serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'due_date',
            'created_at',
            'status',
            'employee'
        )

    def get_status(self, obj) -> Any:
        return obj.status.name
    
    def get_status(self, obj):
        return EmployeeSerializer(obj.employee).data
    
    def update(self, instance, validated_data) -> None:
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status_id = validated_data.get('status_id', instance.status_id)
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.due_date = validated_data.get('due_date', instance.due_date)

        instance.save()

        return instance
