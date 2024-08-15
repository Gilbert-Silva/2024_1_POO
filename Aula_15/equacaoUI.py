import streamlit as st
import pandas as pd
from equacao import Equacao

class EquacaoUI:
    def main():
        st.header("Equação do 2º Grau: a*x² + b*x + c")
        a = st.number_input("a")
        b = st.number_input("b")
        c = st.number_input("c")
        if st.button("Calcular"):
            eq = Equacao(a, b, c)
            st.write(eq)
            st.write(f"Delta = {eq.delta()}")
            if eq.tem_raizes_reais():
                st.write(f"x1 = {eq.x1()}")
                st.write(f"x2 = {eq.x2()}")
                d = abs(eq.x1()-eq.x2())
                if d == 0: d = 4
                xmin = eq.x2() - d/2
                xmax = eq.x1() + d/2
            else:
                st.write("Não tem raízes reais")   
                xmin = -10
                xmax = 10 
            px = []
            py = []
            x = xmin
            while x < xmax * 1.005:
                px.append(x)
                py.append(eq.y(x))
                x += (xmax - xmin) / 50
            #st.write(px)
            #st.write(py)
            dic = { "x" : px, "y" : py }
            chart_data = pd.DataFrame(dic)
            st.line_chart(chart_data, x = "x", y = "y")    

EquacaoUI.main()
