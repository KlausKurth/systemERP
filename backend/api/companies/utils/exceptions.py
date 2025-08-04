'''
utils.py normalmente é criado para organizar funções auxiliares ou utilitárias que não se encaixam diretamente em views.py, models.py, ou serializers.py, mas que ainda são importantes para a lógica do app.
'''

'''
APIException é uma exceção do DRF usada para retornar erros bonitinhos na API. Você pode e deve customizar subclasses dela para seus erros de negócio, como "Grupo não encontrado", "Campos obrigatórios ausentes", etc.
'''

from rest_framework.exceptions import APIException

class NotFoundEmployee(APIException):
    status_code = 404
    default_detail = 'Funcionario não encontrado'
    default_code = 'not_found_employee'

class NotFoundGroup(APIException):
    status_code = 404
    default_detail = 'O grupo não foi encontrado'
    default_code = 'not_found_group'

class RequiredFields(APIException):
    status_code = 404
    default_detail = 'Envie os campos no padrão correto'
    default_code = 'error_required_field'

class NotFoundTaskStatus(APIException):
    status_code= 404
    default_detail = 'Status da tarefa não foi encontrado'
    default_code = 'not_found_task_status'

class NotFoundTask(APIException):
    status_code = 404
    default_detail = 'Tarefa não encontrada'
    default_code = 'not_found_task'

