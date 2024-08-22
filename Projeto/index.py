from templates.manterclienteUI import ManterClienteUI
#from templates.mantercategoriaUI import ManterCategoriaUI
#from templates.manterprodutoUI import ManterProdutoUI
#from templates.reajustarprecoUI import ReajustarPrecoUI
#from templates.loginUI import LoginUI
#from templates.abrircontaUI import AbrirContaUI
from views import View

import streamlit as st

class IndexUI:

#  def menu_visitante():
#    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
#    if op == "Login": LoginUI.main()
#    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Categorias", "Manter Produtos", "Reajustar Preços"])
    if op == "Manter Clientes": ManterClienteUI.main()
    #if op == "Manter Categorias": ManterCategoriasUI.main()
    #if op == "Manter Produtos": ManterProdutosUI.main()
    #if op == "Reajustar Preços": ReajustarPrecosUI.main()

#  def menu_cliente():
#    op = st.sidebar.selectbox("Menu", ["Agenda de Hoje"])
#    if op == "Agenda de Hoje": AgendaHojeUI.main()

#  def btn_logout():
#    if st.sidebar.button("Logout"):
#      del st.session_state["cliente_id"]
#      del st.session_state["cliente_nome"]
#      st.rerun()

  def sidebar():
    IndexUI.menu_admin()

#    if "cliente_id" not in st.session_state:
#      IndexUI.menu_visitante()   
#    else:
#      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
#      if st.session_state["cliente_nome"] == "admin": IndexUI.menu_admin()
#      else: IndexUI.menu_cliente()
#      IndexUI.btn_logout()  

  def main():
#    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()