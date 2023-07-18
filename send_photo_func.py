from config import bot

def send_photo(path,message):
          with open(path,'rb') as file:
           bot.send_photo(message.chat.id,file)
