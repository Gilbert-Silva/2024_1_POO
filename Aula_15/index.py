import streamlit as st

class Index:
    def main():
        pages = {
            "Opções": [
                st.Page("retanguloUI.py", title="Retângulo"),
                st.Page("equacaoUI.py", title="Equação"),
            ]
        }

        pg = st.navigation(pages)
        pg.run()

Index.main()
           
