# Interface GUI da aplicação
from nicegui import ui
from storage import coletar_projetos
from storage import criar_tarefa

# ========== Objetos ==========
# Cabeçalho
# Menu Lateral
#   Botão Criar Tarefa
#   Botão Salvar Projeto
#   Botão Carregar Projeto
# Nome do Projeto
# Descrição
# Colunas
#   Cartões de Tarefas

def cabecalho(titulo):
    with ui.header().classes("bg-blue items-center justify-center text-white py-6"):
        ui.label(titulo).classes("text-3xl font-bold absolute-center")

def menu_lateral(lista_projeto):
    lista = coletar_projetos()
    with ui.left_drawer(value=True).classes("bg-slate-100 p-4") as menu_lateral:
        ui.label("Menu").classes("text-lg mb-1")
        ui.button("Nova Tarefa", icon="add", on_click=janela_nova_tarefa).props("flat").classes("w-full justify-start")
        ui.button("Salvar Projeto", icon="save", on_click=lambda: ui.notify("Salvar Projeto")).props("flat").classes("w-full justify-start")
        ui.separator()
        ui.label("Projetos Salvos").classes("text-lg mb-1")
        for projeto in lista_projeto:
            with ui.item().classes("w-full p-2 gap-0.5 justify-between"):
                with ui.item_section():
                    ui.item_label(projeto[1]).classes("text-base font-semibold")
                    ui.item_label(projeto[0]).classes("text-xs text-gray-400")
                ui.button(icon="open_in_new", on_click=lambda: ui.notify("Abrir Projeto")).props("flat dense")
                ui.button(icon="delete", on_click=lambda: ui.notify("Apagar Projeto")).props("flat dense")

def corpo(lista_tarefas=[]):
    with ui.element("div").classes("items-center justify-center"):
        ui.label("Projeto").classes("text-lg font-semibold mb-1 text-center")
        ui.label("Descrição").classes("text-center")
    with ui.row().classes("w-full justify-center "):
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("A Fazer").classes("text-lg font-semibold")
            for tarefa in lista_tarefas:
                if tarefa[3] == "todo":
                    card_tarefa(tarefa[0], tarefa[1], tarefa[2], tarefa[3])
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("Em Andamento").classes("text-lg font-semibold")
            for tarefa in lista_tarefas:
                if tarefa[3] == "doing":
                    card_tarefa(tarefa[0], tarefa[1], tarefa[2], tarefa[3])
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("Concluído").classes("text-lg font-semibold")
            for tarefa in lista_tarefas:
                if tarefa[3] == "done":
                    card_tarefa(tarefa[0], tarefa[1], tarefa[2], tarefa[3])

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
        desc_tarefa = ui.input(label="Descrição").classes("w-full")
        with ui.row().classes("w-full justify-end"):
            ui.button("Cancelar", on_click=dialogo.close).props("flat")
            ui.button("Criar Tarefa", on_click=lambda: tarefa_nova(nome_tarefa.value, desc_tarefa.value))
    dialogo.open()

def tarefa_nova(nome, desc):
    lista = criar_tarefa(nome, desc)
    card_tarefa(lista[0],lista[1], lista[2], lista[3])
