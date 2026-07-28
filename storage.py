# Arquivo de armazenamento de projetos, com suas respectivas tarefas
from classes import Projeto
from classes import Tarefa
import config
from config import ARQUIVO_PROJETO
from config import ARQUIVO_TAREFAS
import json
import uuid

# ========== Funções de Arquivos ==========
def ler_arquivos():
    with open(ARQUIVO_PROJETO, "r", encoding="utf-8") as arquivo:
        config.dict_projetos = json.load(arquivo)
    with open (ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
        config.dict_tarefas = json.loads(arquivo)
def salvar_arquivos(dict_projeto=0, dict_tarefa=0):
    if dict_projeto is not 0:
        with open(ARQUIVO_PROJETO, "w", encoding="utf-8") as arquivo:
            json.dumps(dict_projeto, arquivo, indent=4, ensure_ascii=False)
    if dict_tarefa is not 0:
        with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
            json.dumps(dict_tarefa, arquivo, indent=4, ensure_ascii=False)

# ========== Funções de Projetos ==========
def apagar_projeto(id_projeto):
    del config.dict_projeto[id_projeto]
    for id_tarefa, tarefa in config.dict_tarefas:
        if tarefa["projeto"] == id_projeto:
            del config.dict_tarefas[id_tarefa]
    salvar_arquivos(dict_projeto=config.dict_projetos, dict_tarefa=config.dict_tarefas)
def criar_projeto(titulo, descricao):
    id_projeto = str(uuid.uuid4())
    projeto = Projeto(id_projeto, titulo, descricao)
    config.dict_projeto[id_projeto] = projeto.dicionario_projeto()
    salvar_arquivos(dict_projeto=config.dict_projetos)

# ========== Funções de Tarefas ==========
def criar_tarefa(nome, descricao):
    id_tarefa = str(uuid.uuid4())
    tarefa = Tarefa(id_tarefa, nome, descricao)
    config.dict_tarefas[id_tarefa] = tarefa.dicionario_tarefa()
    salvar_arquivos(dict_tarefa=config.dict_tarefas)
def mover_tarefa(id_tarefa, novo_status):
    with config.dict_tarefas[id_tarefa] as tarefa:
        tarefa["status"] = novo_status
def apagar_tarefa(id_tarefa):
    del config.dict_tarefas[id_tarefa]
    salvar_arquivos(dict_tarefa=config.dict_tarefas)
