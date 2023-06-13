import telebot
from telebot.types import ReplyKeyboardMarkup,KeyboardButton,Message
class Bot(telebot.TeleBoot):
    def __init__ (self,token)
    self.featuresMarkup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    self.featuresMarkup.add(
        KeyboardButton('Взлом пентагона👨‍💻'),
        KeyboardButton('Калькулятор💻'),
        KeyboardButton('Рандомный стикер❓'),
        KeyboardButton('Игра 9 жизней🎰'),
        KeyboardButton('Искать видео🔎'),
        KeyboardButton('Инфа🛑')
    )
    self.register_message_handler(callback = self.on_start,commands = ['start'])
    self.register_message_handler(callback = self.on_other_message)
    def on_start(self,message:Message):
        pass


    
    def on_other_message(self,message):
        pass


    def on_none_state(self,userId,text,name):
        pass