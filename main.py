from chatterbot import ChatBot

#create chatbot instance
bot = ChatBot('Samantha')

#create object of chatbot class with storage adapter

bot = ChatBot(
    'Samantha',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter', #specifies the type of storage adapter to use for storing chatbot's training data and conversation history
    database_uri = 'sqlite:///database.sqlite3' #specifies location of SQLite database
)

