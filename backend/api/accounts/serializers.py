# Serializer é para converter modelos Python (Django ORM) em JSON para APIs REST.
#Validar e transformar dados de entrada (por exemplo, de um POST) em instâncias do modelo.
#É essencial para transformar os dados da aplicação em algo que o front-end (ou outra API) possa entender.


from rest_framework import serializers

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email'
        ]