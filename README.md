# QA Python Automation

Projeto de automação de testes web utilizando Python, Pytest e Selenium.

## 🎯 Objetivo

Este projeto foi criado para praticar e demonstrar conhecimentos básicos de automação de testes de software.

Os testes são realizados no site SauceDemo.

## 🛠️ Tecnologias utilizadas

- Python
- Pytest
- Selenium
- Google Chrome
- VS Code

## 🧪 Testes automatizados

Atualmente, o projeto possui testes relacionados ao login:

- Login com usuário e senha válidos
- Login com senha inválida
- Login com usuário inválido

## 📁 Estrutura do projeto

```text
qa-python-automation/
├── .venv/
├── tests/
│   └── test_basic.py
├── .gitignore
├── README.md
└── requirements.txt

## ▶️ Como executar o projeto

### 1. Clonar o repositório

Depois que o projeto estiver disponível no GitHub, clone o repositório utilizando:

bash
git clone URL_DO_REPOSITORIO

### 2. Entrar na pasta do projeto

Depois de clonar o projeto, entre na pasta utilizando:

bash
cd qa-python-automation

### 3. Criar o ambiente virtual

Crie um ambiente virtual para manter as dependências do projeto organizadas:

bash
python -m venv .venv

### 4. Ativar o ambiente virtual no Windows

Ative o ambiente virtual utilizando:

powershell
.venv\Scripts\Activate.ps1

Depois da ativação, o terminal deverá apresentar (.venv) no início da linha.

### 5. Instalar as dependências

Instale as bibliotecas necessárias para executar os testes:

bash
pip install -r requirements.txt

O arquivo requirements.txt contém as dependências utilizadas no projeto, como Pytest e Selenium.

### 6. Executar os testes

Depois de configurar o ambiente, execute os testes automatizados utilizando:

bash
python -m pytest -v

O Pytest irá localizar e executar os testes disponíveis dentro da pasta tests.

## 🔎 Resultado esperado

Após executar os testes, o Pytest deverá apresentar no terminal o resultado de cada teste.

Exemplo:

text
3 passed

Isso significa que os três testes automatizados foram executados com sucesso.

## 📌 Objetivo profissional

Este projeto faz parte do meu portfólio de QA e representa minha evolução no aprendizado de testes automatizados.

O objetivo é continuar expandindo o projeto com novos cenários de teste, validações e diferentes técnicas de automação utilizando Python, Pytest e Selenium.