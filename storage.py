# Arquivo de armazenamento de projetos, com suas respectivas tarefas
from classes import Projeto
from classes import Tarefa
import config
import json
from json import JSONDecodeError
import uuid

# ========== Funções de Arquivos ==========
def ler_arquivos():
    try:
        with open(config.ARQUIVO_PROJETO, "r", encoding="utf-8") as arquivo:
            config.dict_projetos = json.load(arquivo)
    except (JSONDecodeError, FileNotFoundError):
        dict = {}
        salvar_projetos_arquivo(dict)
    try:
        with open (config.ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            config.dict_tarefas = json.load(arquivo)
    except (JSONDecodeError, FileNotFoundError):
        dict = {}
        salvar_tarefas_arquivo(dict)  
def salvar_arquivos(dict_projeto={}, dict_tarefa={}):
    if dict_projeto != {}:
        salvar_projetos_arquivo(dict_projeto)
    if dict_tarefa != {}:
        salvar_tarefas_arquivo(dict_tarefa)
def salvar_projetos_arquivo(dict_projeto):
    with open(config.ARQUIVO_PROJETO, "w", encoding="utf-8") as arquivo:
        json.dump(dict_projeto, arquivo, indent=4, ensure_ascii=False)
def salvar_tarefas_arquivo(dict_tarefa):
    with open(config.ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(dict_tarefa, arquivo, indent=4, ensure_ascii=False)

# ========== Funções de Projetos ==========
def apagar_projeto(id_projeto):
    del config.dict_projeto[id_projeto]
    for id_tarefa, tarefa in config.dict_tarefas:
        if tarefa["projeto"] == id_projeto:
            del config.dict_tarefas[id_tarefa]
    salvar_arquivos(dict_projeto=config.dict_projetos, dict_tarefa=config.dict_tarefas)
def criar_projeto(titulo, descricao, id_projeto=""):
    if id_projeto == "":
        id_projeto = str(uuid.uuid4())
    projeto = Projeto(id_projeto, titulo, descricao)
    id_projeto, dict_projeto = projeto.dicionario_projeto()
    config.dict_projetos[id_projeto] = dict_projeto
    salvar_arquivos(dict_projeto=config.dict_projetos)
    config.projeto_ativo = id_projeto

# ========== Funções de Tarefas ==========
def criar_tarefa(nome, descricao):
    id_tarefa = str(uuid.uuid4())
    tarefa = Tarefa(id_tarefa, config.projeto_ativo, nome, descricao)
    id_tarefa, dict_tarefa = tarefa.dicionario_tarefa()
    config.dict_tarefas[id_tarefa] = dict_tarefa
    salvar_arquivos(dict_tarefa=config.dict_tarefas)
def avancar_tarefa(id_tarefa):
    for id_task, tarefa in config.dict_tarefas.items():
        if id_task == id_tarefa:
            match tarefa["status"]:
                case "todo": tarefa["status"] = "doing"
                case "doing": tarefa["status"] = "done"
def retornar_tarefa(id_tarefa):
    for id_task, tarefa in config.dict_tarefas.items():
        if id_task == id_tarefa:
            match tarefa["status"]:
                case "doing": tarefa["status"] = "todo"
                case "done": tarefa["status"] = "doing"
def apagar_tarefa(id_tarefa):
    del config.dict_tarefas[id_tarefa]
    salvar_arquivos(dict_tarefa=config.dict_tarefas)
