import numpy as np
import matplotlib.pyplot as plt
from langchain_community.embeddings import OllamaEmbeddings


# Fornecer um texto simples
texto = ["Ollama é uma poderosa ferramenta de embedding",
         "O arquivo está codificado",
         "Olá, Mundo!!",
         "nome",
         "hit yourself"]

# Define o modelo de embeddings

valor = OllamaEmbeddings(model="mxbai-embed-large")
vetor = valor.embed_documents(texto)

# Mostra o tamanho dos embeddings
embedding_tamanho = len(vetor)
tamanho_vetor = len(vetor[:2])
print(f'O tamanho do embedding é: {embedding_tamanho}')

#Exibir o vetor de embeddings:
print(f'Total: {tamanho_vetor}')

