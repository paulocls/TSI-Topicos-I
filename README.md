# TSI-Topicos-I
Tópicos Avançados em Sistema para Internet I

1. Descrição do arquivo "avaliacao3.py".
Desenvolver um script em Python ou um notebook Jupyter que execute as seguintes ações:
1.Conectar ao Ollama localmente.
2.Fornecer um texto simples (por exemplo, uma frase curta em português ou inglês).
3.Gerar os vetores de embeddings correspondentes ao texto utilizando o Ollama.
4.Exibir o vetor de embeddings, seja de forma integral ou por meio de um sumário, como o tamanho do vetor e alguns valores iniciais.

2. Descrição do arquivo "avaliacao5.py".
Criação do Banco de Dados Vetorial. Utilize textos de sua preferência (por exemplo, textos relacionados a Inteligência Artificial ou Redes Neurais). Divida o texto em chunks. Gere embeddings para cada chunk. Insira os embeddings gerados em um banco de dados vetorial utilizando FAISS. 
Implementação do RetrievalQA. Configure o módulo RetrievalQA para se conectar ao banco de dados vetorial criado. Crie um pipeline que:
Receba uma pergunta do usuário. Converta a pergunta em embeddings. Busque os embeddings mais próximos no banco de dados vetorial.
Retorne uma resposta com base no conteúdo mais relevante encontrado.

3. Descrição do arquivo "avaliacao7.py".
Passo 1: Transcrição de Áudio com Whisper
A aplicação deve receber um arquivo de áudio em formato .wav ou .mp3.
Utilizar o modelo Whisper para transcrever o conteúdo do áudio.
Passo 2: Extração de Pontos-Chave com Ollama
O texto transcrito será enviado ao Ollama.
O Ollama processará o texto e retornará um resumo contendo os principais pontos-chave.
