import telebot
from telebot.types import ReplyKeyboardMarkup,KeyboardButton,Message
from .datab import Database

class Bot(telebot.TeleBot):
    def __init__ (self,token):
        super().__init__(token)
        self.datab = Database('user.json')
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
        self.register_message_handler(callback = self.on_info,commands = ['info'])
        self.register_message_handler(callback = self.on_other_message)

    def on_start(self,message:Message):
        userId = message.from_user.id
        if self.datab.user_exists(userId):
            name = message.from_user.full_name
            self.send_message(userId,'Hello, ' + name)
        else:
            self.datab.create_user(userId)
            self.send_message(userId,'Вас приветсвует бот!',reply_markup=self.featuresMarkup)
    def on_info(self,message:Message):
        userId = message.from_user.id
        self.send_message(userId,'Это мой первый бот,пока что он не доработан,но скоро будет многофункциональным',reply_markup=self.featuresMarkup)

    
    def on_other_message(self,message:Message):
        userId = message.from_user.id
        userState = self.datab.get_user(userId)['state']
        self.on_none_state(userId,message.text,message.from_user.first_name)


    def on_none_state(self,userId,text,name):
        if text == 'Взлом пентагона👨‍💻':
            pass
        elif text == 'Калькулятор💻':
            pass
        elif text == 'Рандомный стикер❓':
            pass
        elif text == 'Игра 9 жизней🎰':
            pass
        elif text == 'Искать видео🔎':
            pass
        elif text == 'Инфа🛑':
            pass
        else:
            self.send_message(userId,'Я не знаю такого действия!',reply_markup=self.featuresMarkup)

    