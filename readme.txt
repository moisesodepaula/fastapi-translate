# Meu Projeto FastAPI

Este é um projeto simples desenvolvido utilizando o framework FastAPI. O objetivo do projeto é implementar uma API que realiza traduções de texto entre diferentes idiomas.

## Tecnologias Utilizadas

- **FastAPI**: Framework web para construir APIs com Python.
- **Uvicorn**: Servidor ASGI para rodar o FastAPI.
- **Python 3.x**: Linguagem de programação utilizada.

## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Você pode verificar a versão do Python com o seguinte comando:

```bash
python --version

1-Instalando Dependências no terminal
Primeiro, crie um ambiente virtual para o projeto:

py -m venv env

2-Ative o ambiente virtual:

.\env\Scripts\activate

3-instale os requerimentos

pip install -r requirements.txt

4. Rodar o Servidor
Agora você pode rodar o servidor FastAPI utilizando o comando:

uvicorn app:app --reload

Este comando irá rodar o servidor na URL http://127.0.0.1:8000.

--reload: Habilita o modo de recarga automática, para que o servidor seja reiniciado toda vez que você alterar o código.

5- Acessando a Documentação
Depois que o servidor estiver rodando, você pode acessar a documentação interativa da API através do Swagger UI:

Swagger UI: http://127.0.0.1:8000/docs
Essa documentação interativa permite que você faça testes diretamente no navegador, enviando requisições para os endpoints da API.

6- Testando a rota de tradução
a API tem uma rota /translate, você verá algo assim na documentação:

Método: POST
Parâmetros:
source_language: o idioma de origem (ex: "en")
target_language: o idioma de destino (ex: "es")
text: o texto a ser traduzido
Clique no botão "Try it out". Preencha os parâmetros com valores de teste:

source_language: "en"
target_language: "es"
text: "Hello, how are you?"
Clique em "Execute". A API retornará a resposta diretamente na interface.