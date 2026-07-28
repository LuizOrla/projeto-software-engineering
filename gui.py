# Interface GUI da aplicação
from nicegui import ui

def cabecalho(titulo):
    with ui.header().classes("bg-blue items-center justify-center text-white py-6"):
        ui.label(titulo).classes("text-3xl font-bold absolute-center")
@ui.refreshable
def menu_lateral(dict_projetos):
    with ui.left_drawer(value=True).classes("bg-slate-100 p-4") as menu_lateral:
        ui.label("Menu").classes("text-lg mb-1")
        ui.button("Nova Tarefa", icon="add", on_click=janela_nova_tarefa).props("flat").classes("w-full justify-start")
        ui.button("Salvar Projeto", icon="save", on_click=janela_novo_projeto).props("flat").classes("w-full justify-start")
        ui.separator()
        ui.label("Projetos Salvos").classes("text-lg mb-1")
        for id, projeto in dict_projetos:
            with ui.item().classes("w-full p-2 gap-0.5 justify-between"):
                with ui.item_section():
                    ui.item_label(projeto["titulo"]).classes("text-base font-semibold")
                    ui.item_label(id).classes("text-xs text-gray-400")
                ui.button(icon="open_in_new", on_click=lambda: ui.notify("Abrir Projeto")).props("flat dense")
                ui.button(icon="delete", on_click=lambda: ui.notify("Apagar Projeto")).props("flat dense")
@ui.refreshable
def corpo(dict_projeto, id_projeto=""):
    if id_projeto == "" or id_projeto not in dict_projeto:
        label_projeto = "Projeto"
        label_descricao = "Descrição"
    else:
        projeto = dict_projeto[id_projeto]
        label_projeto = projeto["titulo"]
        label_descricao = projeto["descricao"]

    with ui.element("div").classes("items-center justify-center"):
        ui.label(label_projeto).classes("text-lg font-semibold mb-1 text-center")
        ui.label(label_descricao).classes("text-center")
    with ui.row().classes("w-full justify-center "):
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("A Fazer").classes("text-lg font-semibold")
            for id_tarefa, tarefa in dict_projeto[id_projeto]:
                if tarefa["satus"] == "todo":
                    card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("Em Andamento").classes("text-lg font-semibold")
            for id_tarefa, tarefa in dict_projeto[id_projeto]:
                if tarefa["satus"] == "doing":
                    card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("Concluído").classes("text-lg font-semibold")
            for id_tarefa, tarefa in dict_projeto[id_projeto]:
                if tarefa["satus"] == "done":
                    card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])
def card_tarefa(id, nome, descricao, status):
    with ui.card().classes("w-full p-2 gap-0.5 justify-between"):
        ui.label(nome).classes("text-base font-semibold")
        ui.label(f"ID: {id}").classes("text-xs text-gray-400")
        ui.label(descricao).classes("text-sm")
        with ui.row().classes("w-full justify-between items-center"):
            if status in ["doing", "done"]:
                ui.button(icon="arrow_back", on_click=lambda: ui.notify(f"Voltar {nome}")).props("flat dense")
            else:
                ui.element("div")
            if status in ["doing", "todo"]:
                ui.button(icon="arrow_forward", on_click=lambda: ui.notify(f"Avançar {nome}")).props("flat dense")

def janela_nova_tarefa():
    with ui.dialog() as dialogo, ui.card().classes("w-2/5"):
        ui.label("Nova Tarefa")
        nome_tarefa = ui.input(label="Nome da Tarefa").classes("w-full")
        tarefa = nome_tarefa.value()
        desc_tarefa = ui.input(label="Descrição").classes("w-full")
        descricao = desc_tarefa.value()
        with ui.row().classes("w-full justify-end"):
            ui.button("Cancelar", on_click=dialogo.close).props("flat")
            ui.button("Criar Tarefa", on_click=lambda: ui.notify("Nova Tarefa"))
    dialogo.open()
def janela_novo_projeto():
    with ui.dialog() as dialogo, ui.card().classes("w-2/5"):
        ui.label("Salvar Projeto")
        nome_projeto = ui.input(label="Título do Projeto"). classes("w-full")
        projeto = nome_projeto.value()
        desc_projeto = ui.input(label="Descrição").classes("w-full")
        descricao = desc_projeto.value()
        with ui.row().classes("w-full justify-end"):
            ui.button("Cancelar", on_click=dialogo.close).props("flat")
            ui.button("Salvar Projeto", on_click=lambda: ui.notify("Salvar Projeto"))
    dialogo.open()

