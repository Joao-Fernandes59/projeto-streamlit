# 1º Passo: Importar bibliotecas
import streamlit as st
# import pandas as pd
from datetime import date


def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a") as file:
            file.write(f"{nome}, {data_nasc}, {tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


# 2º Passo: Configurar página (Título e ícone)
st.set_page_config(page_title=("Cadastro de Clientes"), page_icon="📓")

# 3º Passo: Criar título com linha de separação
st.title("Cadastro de Clientes")
st.divider()

# 4º Passo: Criar uma página para Consulta - Consulta
# No explorador do VS Code, Cria pasta [pages] e dentro dela
# o arquivo Consulta.py

# 5º Passo: Entrada de dados dos clientes
nome = st.text_input("Digite o nome do cliente", key="nome_cliente")

dt_nasc = st.date_input("Data Nascimento", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de Cliente", ["Pessoa Física", "Pessoa Jurídica"])

# 6º Passo: Criar botão para o evento de gravar dados
btn_cadastrar = st.button(
    "Cadastrar", on_click=gravar_dados, args=[nome, dt_nasc, tipo]
)

# 7º Passo: Criar função gravar_dados com os parâmetros:
#           (nome, data_nasc, tipo) ⬆️

# 8º Passo: Verificação da entrada dos dados do cliente
if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✅")
    else:
        st.error("Houve algum problema no cadastro", icon="❌")

# 9º Passo: Criar o arquivo clientes.csv, no explorador do VS Code,
#           para gravação dos dados dos clientes: nome,data_nascimento,tipo

# 10º Passo: incluir na função gravar_dados, rotina de gravação do arquivo
#            clientes.csv

# 11º Passo: Criar rotina de consulta na página Consulta.py
