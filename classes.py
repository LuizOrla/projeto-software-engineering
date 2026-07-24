# Classes pertinentes à aplicação

# ========== Projetos ==========
# Atributos
#   ID
#   Título
#   Descrição
#   Tarefas

class Projeto:
    """
    Estrutura do dicionário:
    ```
    dict_projeto = {
        "id_projeto": {
            "titulo": Nome do Projeto,
            "descricao": Descrição do Projeto,
            "tarefas": {
                "id_tarefa": {
                    "nome": Nome da Tarefa,
                    "descricao_tarefa": Descrição da Tarefa,
                    "status": Status da Tarfa
                }
            }
        }
    }
    """
    def __init__(self, id, titulo, descricao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.tarefas = {}

# ========== Tarefa ==========
# Atributos
#   ID
#   Título
#   Descrição
#   Status
class Tarefas:
    def __init__(self, id, nome, descricao, status="todo"):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.status = status