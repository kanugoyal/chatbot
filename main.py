from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('Chatbot')
trainer= ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

#print(chatbot.get_response("what is computer"))

while True:
    query = input(">>>")
    print(chatbot.get_response(Statement(text = query, search_text = query)))
