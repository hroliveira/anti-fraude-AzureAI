import streamlit as st
from utils.funcoes import show_image_and_validation
from services.blob_service import upload_blob
from services.credit_card_service import analize_cradit_card

def configure_interface():
    st.title("Upload de Arquivo")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file
        #Enviar para o blob storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
          st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
          credit_card_info = analize_cradit_card #Chamar a função de detecção de informações de cartão de crédito
          show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")


        
    if __name__ == "__main__":
        configure_interface