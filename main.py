import chainlit as cl

# Define uma função assíncrona que será chamada quando uma mensagem for recebida
@cl.on_message
async def main(message: cl.Message):
    # Sua lógica personalizada vai aqui ...
    # Verifica se a palavra "python" está presente no conteúdo da mensagem, ignorando maiúsculas e minúsculas
    if "python" in message.content.lower():
        resposta = "Parabéns, você está aprendendo uma boa linguagem!"
    else:
        resposta = "Já pensou em aprender Python?"

    # Envie uma resposta de volta ao usuário
    await cl.Message(content=resposta).send()


# EXECUTAR OS COMANDOS ABAIXO NO TERMINAL
"""
1. chainlit run main.py
2. chainlit hello
"""