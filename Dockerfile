# Imagem base
FROM python:3.10.9-slim-buster

# Define o diretório de trabalho
WORKDIR /app

# Copia o código para o container
COPY . /app

# Instala as dependências
RUN pip install -r requirements.txt

# Expõe a porta 5000
EXPOSE 5000

# Define o comando de inicialização
CMD ["python", "app.py"]
