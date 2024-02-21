# README

Este é um exemplo de um bot simples em Python usando a biblioteca `chainlit` para interagir com o Discord. Este bot verifica mensagens recebidas e responde de acordo com o conteúdo da mensagem.

## Funcionalidades

- Quando uma mensagem é recebida, o bot verifica se a palavra "python" está presente no conteúdo da mensagem, ignorando maiúsculas e minúsculas.
- Se a palavra "python" estiver presente, o bot responde com "Parabéns, você está aprendendo uma boa linguagem!".
- Caso contrário, o bot responde com "Já pensou em aprender Python?".

## Requisitos

- Python 3.6 ou superior
- Biblioteca `chainlit`

## Como executar

1. Instale a biblioteca `chainlit` via pip:

```bash
pip install chainlit
```

2. Execute o arquivo `main.py` usando `chainlit`:

```bash
chainlit run main.py
```

3. Após o bot estar em execução, você pode interagir com ele no Discord, e ele responderá de acordo com a lógica definida.

## Comandos úteis

- Para testar se o bot está online, você pode usar o comando:

```bash
chainlit hello
```

<div align="center">
<img src="https://github.com/mario-evangelista/explorando-recursos-IA-generativa-Chainlit/assets/121322767/fd608692-f1ed-44e4-8e19-d889dc882709" width="700px" />
</div>
<br>

Este bot é apenas um exemplo básico. Sinta-se à vontade para personalizá-lo e adicionar mais funcionalidades conforme necessário!
