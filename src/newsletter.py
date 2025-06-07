import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv() 
openrouter_key = os.getenv("OPENROUTER_API_KEY")
remetente = os.getenv("EMAIL_ADDRESS")
senha_app = os.getenv("EMAIL_APP_PASSWORD")
destinatario = os.getenv("EMAIL_RECIPIENT")

# Palavra-chave para busca
print("")
query = input("Digite uma palavra chave: ")
url = f"https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"

# Coleta do RSS
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")
items = soup.find_all("item")

noticias = []

# Extrair as 3 primeiras notícias
for item in items[:3]:
    descricao_html = item.description.text
    descricao_soup = BeautifulSoup(descricao_html, 'html.parser')
    
    noticia = {
        "headline": item.title.text,
        "descrição": descricao_soup.get_text(),
        "link_google": item.link.text
    }
    noticias.append(noticia)

# Montar o prompt com as 3 notícias
conteudo = "\n\n".join([
    f"Notícia {i+1}:\nHeadline: {n['headline']}\nDescrição: {n['descrição']}\nLink: {n['link_google']}"
    for i, n in enumerate(noticias)
])

prompt = f"Leia as três notícias abaixo e escreva um resumo unificado e detalhado em tópico:\n\n{conteudo}\n\nResumo:"

# Enviar para OpenRouter
openrouter_key = openrouter_key
headers = {
    "Authorization": f"Bearer {openrouter_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://chat.openai.com/",
    "X-Title": "Resumo de notícias sobre dólar"
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(data))

# Verificar conteúdo da resposta
resposta = response.json()

if "choices" in resposta:
    print("\nResumo das notícias:\n")
    print(resposta["choices"][0]["message"]["content"])

    # Resultado gerado pelo modelo
    resumo = resposta["choices"][0]["message"]["content"]

    # Dados do e-mail
    remetente = remetente
    senha_app = senha_app
    destinatario = destinatario 

    # Construir o e-mail
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = f"Resumo das notícias sobre '{query}'"
    mensagem.attach(MIMEText(resumo, "plain"))

    # Enviar via servidor SMTP do Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remetente, senha_app)
        servidor.send_message(mensagem)

    print("\n✅ E-mail enviado com sucesso.\n")

else:
    print("\nErro na resposta da API:")
    print(json.dumps(resposta, indent=2, ensure_ascii=False))

