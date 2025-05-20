# Simulador de pipeline de ingestão
def ingest_documents(folder_path):
    """
    Fluxo simulado:
    1. Carregar documentos (PDF, DOCX, TXT)
    2. Extrair texto e metadados
    3. Aplicar pré-processamento (NLP básico)
    4. Gerar representações intermediárias
    """
    documents = []
    # Simulação de processamento
    for file in simulated_files:
        doc = {
            "id": generate_uuid(),
            "content": extract_text(file),
            "metadata": extract_metadata(file),
            "embeddings": None  # Seria gerado com Azure AI
        }
        documents.append(doc)
    return documents