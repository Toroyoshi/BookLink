# Usa uma imagem base de Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o contêiner
COPY . /app

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Expõe a porta que o serviço irá rodar
EXPOSE 6000

# Comando para rodar o serviço
CMD ["python", "app.py"]