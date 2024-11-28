
import os
import streamlit as st

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagen enviada", use_column_width=True)
    st.write("Resultado de validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color : green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")
        
    #st.write("Informações de cartão de crédito encontradas: ")
    #st.write(credit_card_info)