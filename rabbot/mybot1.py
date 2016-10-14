from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot("mybot1")
chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train("chatterbot.corpus.english")
response=chatbot.get_response("hello,what's your name?")
print (response)