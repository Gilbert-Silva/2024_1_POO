import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculo com Retângulo")
        b = st.text_input("Informe o valor da base")
        h = st.text_input("Informe o valor da altura")
        if st.button("Calcular"):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(r.calc_area())
            st.write(r.calc_diagonal())

RetanguloUI.main()