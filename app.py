import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Proporcionalidad simple.')

with st.container(border=True):
    st.subheader('Proporcionalidad directa:')
    st.markdown('''Las magnitudes son directamente proporcionales si al aumentar una, la otra también aumenta y al disminuir una, la otra también disminuye. ''')
    st.subheader("**Ejemplo:**")
    st.markdown('En una fábrica de balones, cada trabajador fabrica 5 balones al día. Si la empresa contrata más trabajadores, el número de balones que se fabrica será mayor.')
    df = pd.DataFrame({
    'Trabajadores': [1, 2, 3, 5],
    'Balones': [5, 10, 15, 25],
    })
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.markdown('''A medida que aumenta el número de trabajadores, lo hace el número de balones.

Estas dos magnitudes (número de trabajadores y de balones) mantienen una relación de proporcionalidad directa.

Si dividimos el número de balones entre el de trabajadores, obtenemos un resultado constante:$$\\frac{balones}{trabajadores}$$

$$
\\frac{5}{1}=5,   \\frac{10}{2}=5,   \\frac{15}{3}=5,   \\frac{25}{5}=5
$$
Este número se denomina **constante de proporcionalidad** o **razón.**'''
)

with st.container(border=True):
    st.subheader('Proporcionalidad inversa:')
    st.markdown('''cuando una magnitud crece y la otra disminuye proporcionalmente, se le llama proporcionalidad Inversa. Dos magnitudes son inversamente proporcionales si al multiplicar (o dividir) una de ellas por un número, la otra queda dividida (o multiplicada) por el mismo número. ''')
    st.subheader("**Ejemplo:**")
    st.markdown('El tiempo que se tarda en construir una casa entre 2 obreros es 10 meses. Si el número de obreros aumenta, el tiempo que se tarda es menor.')
    df2 = pd.DataFrame({
    "Obreros": [2, 4, 5],
    "Meses": [10, 5, 4],
    })
    st.dataframe(df2, hide_index=True, use_container_width=True)
    st.markdown('''Estas dos magnitudes mantienen una relación de proporcionalidad inversa: cuando una magnitud aumenta, la otra disminuye y viceversa.

La constante de proporcionalidad se calcula multiplicando las magnitudes: $${obreros}*{meses}$$

$$
{2}*{10}=20,   {4}*{5}=20,   {5}*{4}=20
$$
''')

with st.container(border=True):
    st.subheader('Simulación:')
    st.markdown("Ingrese los valores de las magnitudes para la simulación (de **a,b,c** es x y **d,e,f** es y).")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        a=int(st.number_input('a:', value=1))
    with col2:
        b=int(st.number_input('b:', value=1))
    with col3:
        c=int(st.number_input('c:', value=1))
    with col4:
        d=int(st.number_input('d:', value=1))
    with col5:
        e=int(st.number_input('e:', value=1))
    with col6:
        f=int(st.number_input('f:', value=1))

    df3 = pd.DataFrame({
        "x": [{a}, {b}, {c}],
        "y": [{d}, {e}, {f}],
        })
    tabla = st.dataframe(df3, hide_index=True, use_container_width=True)


    if a<b<c and d>e>f:
        g= a*d
        h= b*e
        i= c*f
        if g==h==i:
            st.markdown('Las magnitudes son **inversamente proporcionales**:')
            df4 = pd.DataFrame({
                "Proporcionalidad": [g, h, i],
                })
            st.dataframe(df4, hide_index=True, use_container_width=True)
        else:
            st.markdown('Las magnitudes no son **inversamente proporcionales:**')
            df4 = pd.DataFrame({
                "Proporcionalidad": [g, h, i],
                })
            st.dataframe(df4, hide_index=True, use_container_width=True)
    elif a>b>c and d>e>f:
        j= d/a
        k= e/b
        l= f/c
        if j==k==l:
            st.markdown('Las magnitudes son **directamente proporcionales**:')
            df5 = pd.DataFrame({
                "Proporcionalidad": [j, k, l],
                })
            st.dataframe(df5, hide_index=True, use_container_width=True)
        else:
            st.markdown('Las magnitudes no son **directamente proporcionales:**')
            df5 = pd.DataFrame({
                "Proporcionalidad": [j, k, l],
                })
            st.dataframe(df5, hide_index=True, use_container_width=True)

