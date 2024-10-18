from config import connect_str, container_name, endpoint, key
from upload import upload_document
from process import process_document
from analysis import identificar_fraude, validar_autenticidade

def main():
    file_path = "seuarquivo.pdf"

    # Upload do documento
    upload_document(file_path, connect_str, container_name)

    # Análise do documento
    result = process_document(file_path, endpoint, key)

    # Identificação de fraudes e validação de autenticidade
    identificar_fraude(result)
    validar_autenticidade(result)

if __name__ == "__main__":
    main()
