# Arquivo principal de orquestração

from classes import Projeto
from classes import Tarefas
from storage import coletar_projetos
from storage import coletar_tarefas
from storage import atualizar_projetos
from storage import criar_projeto
from storage import apagar_projeto

from gui import cabecalho
from gui import menu_lateral
from gui import corpo

from config import ARQUIVO_STORAGE

from nicegui import ui


lista_proj = coletar_projetos()
# lista_task = coletar_tarefas()

cabecalho("Projeto Teste")
menu_lateral(lista_proj)
corpo()
ui.run()


# Iniciar Aplicação
#   Cabeçalho
#   Menu Lateral
#       Botão Criar Tarefa
#       Botão Salvar Projeto
#       Lista de Projetos
#           Botão Abrir
#           Botão Apagar
#   Colunas Status
#       Tarefas
#           Alterar Status/Mover

# Carregar Projeto
#   Limpar Tarefas
#   Ler Dicionário
#   Carregar Tarefas

# Salvar Projeto
#   Atualizar dicionário

#

# Criar Tarefa
#   Solicitar Nome
