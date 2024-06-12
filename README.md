# Chatbot Simples com NLTK

Este projeto implementa um chatbot simples usando a biblioteca NLTK (Natural Language Toolkit) em Python. O chatbot responde a várias entradas de texto baseadas em padrões predefinidos.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python 3.x instalado em sua máquina. Além disso, você precisará instalar a biblioteca NLTK.

Você pode instalar a biblioteca NLTK executando:

```
pip install nltk
```
# Configuração
Clone este repositório ou copie os arquivos para o seu ambiente de desenvolvimento.

Baixe os recursos necessários do NLTK (só precisa ser feito uma vez):

```
import nltk
nltk.download('punkt')
nltk.download('wordnet')

````
# Uso
Para iniciar o chatbot, execute o script chatbot_nltk.py:

```
python chatbot_nltk.py

```
O chatbot estará pronto para interagir com você. Digite suas perguntas e ele responderá com base nos padrões predefinidos.

# Estrutura do Código
Patterns de Entrada e Respostas: Define padrões de entrada do usuário e as respostas correspondentes.
Funções Principais:
chatbot(): Inicia o chatbot e gerencia o loop de interação com o usuário.
Padrões de Entrada e Respostas
O chatbot responde a várias entradas baseadas em padrões predefinidos. Aqui estão alguns exemplos:

## Saudações:
Entrada: oi, olá, e aí
Resposta: Olá!, Oi!, Como vai?
## Nome:
Entrada: qual é o seu nome?
Resposta: Eu sou um chatbot!, Você pode me chamar de ChatBot., Meu nome é ChatBot.
## Estado:
Entrada: como você está?
Resposta: Estou bem, obrigado por perguntar!, Ótimo, e você?
## Despedida:
Entrada: adeus, tchau, até logo
Resposta: Até logo!, Tchau! Volte em breve.
## Idade:
Entrada: (.*) idade (.*) você, quantos anos você tem?
Resposta: Eu sou um programa de computador, idade não se aplica a mim!
# Novos Padrões:
Entrada: (.*) (feliz|contente)

Resposta: Fico feliz em ouvir isso!, É ótimo ver você feliz!

Entrada: (.*) triste

Resposta: Sinto muito ouvir isso. Posso ajudar de alguma forma?, Às vezes, conversar pode ajudar a lidar com a tristeza.

Entrada: como posso te ajudar?

Resposta: Você pode me perguntar sobre qualquer coisa!, Estou aqui para responder às suas perguntas.

Entrada: o que você gosta de fazer?

Resposta: Adoro conversar com pessoas como você!, Minha função principal é conversar, e eu adoro isso!

Entrada: (.*) (filme|livro) favorito

Resposta: Não assisto filmes ou leio livros, mas ouvi falar de muitos bons!

Entrada: (.*) (comida|comer) favorita

Resposta: Não como, mas ouvi dizer que pizza é muito popular!

Entrada: (.*) (ajuda|ajudar) (.*)

Resposta: Claro, estou aqui para ajudar!, Posso tentar ajudar. Qual é o seu problema?

Entrada: estou entediado

Resposta: Que tal falarmos sobre um tópico interessante?

# Exemplo de Interação
```
Olá! Eu sou um chatbot. Como posso ajudar você hoje?
Você: oi
ChatBot: Oi!
Você: qual é o seu nome?
ChatBot: Eu sou um chatbot!
Você: como você está?
ChatBot: Estou bem, obrigado por perguntar!
Você: sair
ChatBot: Até logo!
```
# Contribuição
Se quiser contribuir com melhorias, sinta-se à vontade para fazer um fork do projeto e enviar um pull request.


# Autor
Desenvolvido por Ariany.