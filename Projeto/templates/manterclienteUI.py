import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
  def main():
    st.header("Cadastro de Clientes")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterClienteUI.listar()
    with tab2: ManterClienteUI.inserir()
    with tab3: ManterClienteUI.atualizar()
    with tab4: ManterClienteUI.excluir()

  def listar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      dic = [] # lista de dicionários, onde cada dicionário é um cliente
      for obj in clientes: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      try:
        View.cliente_inserir(nome, email, fone) #, senha)
        st.success("Cliente inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError:
        st.write("Nome e/ou e-mail inválidos")  

  def atualizar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Atualização de Clientes", clientes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha")
      if st.button("Atualizar"):
        id = op.get_id()
        View.cliente_atualizar(id, nome, email, fone) #, senha)
        st.success("Cliente atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Exclusão de Clientes", clientes)
      if st.button("Excluir"):
        id = op.get_id()
        View.cliente_excluir(id)
        st.success("Cliente excluído com sucesso")
        time.sleep(2)
        st.rerun()