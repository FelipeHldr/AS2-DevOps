# Imagem base
FROM python:3.10.9-slim-buster

# Define o diretório de trabalho
WORKDIR /app

# Copia o código para o container
COPY . .

# Instala as dependências
RUN pip3.10 install Flask

# Expõe a porta 5000
EXPOSE 5000

# Define o comando de inicialização
CMD ["python", "app.py"]
