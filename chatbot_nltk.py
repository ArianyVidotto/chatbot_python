import nltk
import random
from nltk.chat.util import Chat, reflections

# Baixando os recursos
nltk.download('punkt')
nltk.download('wordnet')

# Pares de padrão de entrada e respostas
patterns = [
    (r'oi|olá|e aí', ['Olá!', 'Oi!', 'Como vai?']),
    (r'qual é o seu nome?', ["Eu sou um chatbot!", "Você pode me chamar de ChatBot.", "Meu nome é ChatBot."]),
    (r'como você está?', ["Estou bem, obrigado por perguntar!", "Ótimo, e você?"]),
    (r'adeus|tchau|até logo', ["Até logo!", "Tchau! Volte em breve."]),
    (r'(.*) idade (.*) você|quantos anos você tem?', ["Eu sou um programa de computador, idade não se aplica a mim!"]),
    # Novos padrões e respostas
    (r'(.*) (feliz|contente)', ["Fico feliz em ouvir isso!", "É ótimo ver você feliz!"]),
    (r'(.*) triste', ["Sinto muito ouvir isso. Posso ajudar de alguma forma?", "Às vezes, conversar pode ajudar a lidar com a tristeza."]),
    (r'como posso te ajudar?', ["Você pode me perguntar sobre qualquer coisa!", "Estou aqui para responder às suas perguntas."]),
    (r'o que você gosta de fazer?', ["Adoro conversar com pessoas como você!", "Minha função principal é conversar, e eu adoro isso!"]),
    (r'(.*) (filme|livro) favorito', ["Não assisto filmes ou leio livros, mas ouvi falar de muitos bons!"]),
    (r'(.*) (comida|comer) favorita', ["Não como, mas ouvi dizer que pizza é muito popular!"]),
    (r'(.*) (ajuda|ajudar) (.*)', ["Claro, estou aqui para ajudar!", "Posso tentar ajudar. Qual é o seu problema?"]),
    (r'estou entediado', ["Que tal falarmos sobre um tópico interessante?"]),
    # Padrão de saída
    (r'sair|adeus|tchau|até logo', ["Até logo!", "Tchau! Volte em breve."]),
]

# Criando o chatbot
def chatbot():
    print("Olá! Eu sou um chatbot. Como posso ajudar você hoje?")
    chat = Chat(patterns, reflections)
    while True:
        user_input = input("Você: ")
        response = chat.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == 'sair':
            break

# Função principal
if __name__ == "__main__":
    chatbot()
