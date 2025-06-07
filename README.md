## 📬 Newsletter - Resumo de Notícias com OpenRouter e Envio por E-mail

Este projeto coleta as 3 primeiras notícias do Google News com base em uma palavra-chave digitada pelo usuário, gera um **resumo unificado usando a OpenRouter API (GPT)**, e envia esse resumo por **e-mail**.

---

### 🔧 Requisitos

- Python 3.12+
- Biblioteca [Poetry](https://python-poetry.org/)
- Conta de e-mail com senha de aplicativo (ex: Gmail com 2FA)
- Chave da OpenRouter API

---

### 📁 Estrutura do projeto

```
newsletter_ling_prog/
├── src/
│   └── newsletter.py
├── .env.example
├── .gitignore
├── README.md
├── poetry.lock
└── pyproject.toml
```

---

### ⚙️ Variáveis de ambiente (.env)

Configure suas credenciais no arquivo `.env`:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
EMAIL_ADDRESS=your_email_here
EMAIL_APP_PASSWORD=your_email_app_password
EMAIL_RECIPIENT=recipient_email_here
```

---

### ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/francomansur/newsletter_ling_prog.git
   cd newsletter_ling_prog
   ```

2. Instale as dependências:
   ```bash
   poetry install
   ```

3. Crie o arquivo `.env` com base no `.env.example`.

4. Execute o programa:
   ```bash
   poetry run python src/newsletter.py
   ```

---

### 🧠 O que o programa faz

- Solicita ao usuário uma palavra-chave.
- Busca notícias relacionadas no Google News (via RSS).
- Extrai os títulos, descrições e links das 3 primeiras notícias.
- Monta um prompt com as informações e envia à API da OpenRouter.
- Recebe um resumo em linguagem natural.
- Envia o conteúdo gerado por e-mail ao destinatário informado no `.env`.

---

### 📦 Bibliotecas utilizadas

- `requests`: para chamadas HTTP.
- `BeautifulSoup`: para parse do RSS e HTML da descrição.
- `smtplib` + `email.mime`: para envio de e-mail via SMTP.
- `dotenv`: para carregamento de variáveis de ambiente.

---

### ✅ Exemplo de saída

```text
Digite uma palavra chave: dólar

Resumo das notícias:

- A cotação do dólar caiu devido ao aumento das exportações brasileiras.
- O Banco Central dos EUA sinalizou pausa nos aumentos de juros.
- Investidores estão mais otimistas com a economia global.

✅ E-mail enviado com sucesso.
```

---

### 📬 Contato

Desenvolvido por [Franco Mansur](https://github.com/francomansur)
