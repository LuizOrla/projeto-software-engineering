# Interface GUI da aplicação
from nicegui import ui
import config
import storage

def cabecalho(titulo):
    with ui.header().classes("bg-blue items-center justify-center text-white py-6"):
        ui.label(titulo).classes("text-3xl font-bold absolute-center")
def menu_lateral():
    with ui.left_drawer(value=True).classes("bg-slate-100 p-4") as menu_lateral:
        ui.label("Menu").classes("text-lg mb-1")
        ui.button("Nova Tarefa", icon="add", on_click=janela_nova_tarefa).props("flat").classes("w-full justify-start")
        ui.button("Novo Projeto", icon="add", on_click=janela_novo_projeto).props("flat").classes("w-full justify-start")
        ui.button("Salvar Projeto", icon="save", on_click=janela_novo_projeto).props("flat").classes("w-full justify-start")
        ui.separator()
        ui.label("Projetos Salvos").classes("text-lg mb-1")
        conteudo_projetos()
@ui.refreshable
def conteudo_projetos():
    with ui.column().classes("w-full gap-1"):
        lista_projetos()
def lista_projetos():
    for id_projeto, projeto in config.dict_projetos.items():
        with ui.item().classes("w-full p-2 gap-0.5 justify-between"):
            with ui.item_section():
                ui.item_label(projeto["titulo"]).classes("text-base font-semibold")
                ui.item_label(id_projeto).classes("text-xs text-gray-400")
            ui.button(icon="open_in_new", on_click=lambda _, id_abrir=id_projeto: abrir_projeto(id_abrir)).props("flat dense")
            ui.button(icon="delete", on_click=lambda: ui.notify("Apagar Projeto")).props("flat dense")
@ui.refreshable
def corpo(id_projeto=config.projeto_ativo):
    if config.projeto_ativo == "":
        label_projeto = "Projeto"
        label_descricao = "Descrição do projeto"
        with ui.row().classes("w-full justify-center"):
            with ui.element("div").classes("items-center justify-center"):
                ui.label(label_projeto).classes("text-lg font-semibold mb-1 text-center")
                ui.label(label_descricao).classes("text-center")
        with ui.row().classes("w-full justify-center "):
            with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
                ui.label("A Fazer").classes("text-lg font-semibold")
            with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
                ui.label("Em Andamento").classes("text-lg font-semibold")
            with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
                ui.label("Concluído").classes("text-lg font-semibold")
    else:
        projeto = config.dict_projetos[config.projeto_ativo]
        label_projeto = projeto["titulo"]
        label_descricao = projeto["descricao"]

        with ui.row().classes("w-full justify-center"):
            with ui.element("div").classes("items-center justify-center"):
                ui.label(label_projeto).classes("text-lg font-semibold mb-1 text-center")
                ui.label(label_descricao).classes("text-center")
        with ui.row().classes("w-full justify-center "):
            with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
                ui.label("A Fazer").classes("text-lg font-semibold")
                if id_projeto != "":
                    for id_tarefa, tarefa in config.dict_tarefas.items():
                        if tarefa["projeto"] == id_projeto and tarefa["status"] == "todo":
                            card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])
            with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
                ui.label("Em Andamento").classes("text-lg font-semibold")
                if id_projeto != "":
                    for id_tarefa, tarefa in config.dict_tarefas.items():
                        if tarefa["projeto"] == id_projeto and tarefa["status"] == "doing":
                            card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])
            with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
                ui.label("Concluído").classes("text-lg font-semibold")
                if id_projeto != "":
                    for id_tarefa, tarefa in config.dict_tarefas.items():
                        if tarefa["projeto"] == id_projeto and tarefa["status"] == "done":
                            card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])
def card_tarefa(id, nome, descricao, status):
    with ui.card().classes("w-full p-2 gap-0.5 justify-between"):
        ui.label(nome).classes("text-base font-semibold")
        ui.label(f"ID: {id}").classes("text-xs text-gray-400")
        ui.label(descricao).classes("text-sm")
        with ui.row().classes("w-full justify-between items-center"):
            if status in ["doing", "done"]:
                ui.button(icon="arrow_back", on_click=lambda: move_tarefa(id, "retorna")).props("flat dense")
            else:
                ui.button(icon="delete", on_click=lambda: ui.notify("Apagar Tarefa")).props("flat dense")
            if status in ["doing", "todo"]:
                ui.button(icon="arrow_forward", on_click=lambda: move_tarefa(id, "avanca")).props("flat dense")

def janela_nova_tarefa():
    with ui.dialog() as dialogo, ui.card().classes("w-2/5"):
        ui.label("Nova Tarefa")
        nome_tarefa = ui.input(label="Nome da Tarefa").classes("w-full")
        desc_tarefa = ui.input(label="Descrição").classes("w-full")
        with ui.row().classes("w-full justify-end"):
            ui.button("Cancelar", on_click=dialogo.close).props("flat")
            ui.button("Criar Tarefa", on_click=lambda: nova_tarefa(nome_tarefa.value, desc_tarefa.value, dialogo))
    dialogo.open()
def janela_novo_projeto():
    with ui.dialog() as dialogo, ui.card().classes("w-2/5") as cartao:
        ui.label("Salvar Projeto")
        nome_projeto = ui.input(label="Título do Projeto"). classes("w-full")
        desc_projeto = ui.input(label="Descrição").classes("w-full")
        with ui.row().classes("w-full justify-end"):
            ui.button("Cancelar", on_click=dialogo.close).props("flat")
            ui.button("Salvar Projeto", on_click=lambda: novo_projeto(nome_projeto.value, desc_projeto.value, dialogo))
    dialogo.open()

def move_tarefa(id, direcao):
    match direcao:
        case "avanca": storage.avancar_tarefa(id)
        case "retorna": storage.retornar_tarefa(id)
    corpo.refresh()
def nova_tarefa(nome, descricao, dialogo):
    if config.projeto_ativo == "" or config.projeto_ativo not in config.dict_projetos:
        ui.notify("Crie ou selecione um projeto antes de criar uma tarefa.")
        dialogo.close()
        return
    storage.criar_tarefa(nome, descricao)
    dialogo.close()
    corpo.refresh()

def novo_projeto(nome, descricao, dialogo, id=""):
    storage.criar_projeto(nome, descricao, id)
    dialogo.close()
    corpo.refresh()
    conteudo_projetos.refresh()
def salvar_projeto():
    if config.projeto_ativo == "":
        ui.notify("Nenhum projeto ativo.")
        return
    storage.salvar_arquivos(dict_projeto=config.dict_projetos, dict_tarefa=config.dict_tarefas)
def abrir_projeto(id_projeto):
    config.projeto_ativo = id_projeto
    corpo.refresh(config.projeto_ativo)
