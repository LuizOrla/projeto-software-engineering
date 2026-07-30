# Arquivo principal de orquestração
from storage import ler_arquivos
from gui import cabecalho
from gui import menu_lateral
from gui import corpo
from nicegui import ui
import config

ler_arquivos()

cabecalho("Projeto Teste")
menu_lateral()
corpo()
ui.run()
