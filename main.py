import telebot
from telebot import types

bot = telebot.TeleBot('5310953992:AAFHc7HFRVvF1VPNEgX6yC1zuuBR-OTdlI4')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Генератор списка")
    btn2 = types.KeyboardButton("Максимум")
    btn3 = types.KeyboardButton("Сумма")
    btn4 = types.KeyboardButton("Произведение")
    btn5 = types.KeyboardButton("Факториал")
    btn6 = types.KeyboardButton("Генератор строки")
    btn7 = types.KeyboardButton("Паскаль")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(chat_id,
                     text="Привет! Это 8 урок :) Задание, выполненное Беляевой Дарьей 1-МД-25".format(
                         message.from_user), reply_markup=markup)


    # Получение сообщений от юзера
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
       chat_id = message.chat.id
       ms_text = message.text

       if ms_text == "Генератор списка":
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          # Задание a
          list = [i for i in range(0, 500) if len(str(i)) == 2 and 10 < i < 20]
          bot.send_message(message.chat.id, f'Ваш список: {list}')

       elif ms_text == "Максимум":
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          # Задание b
          from functools import reduce
          max = str(reduce(max, list))
          bot.send_message(chat_id, f'Максимум: {max}', reply_markup=markup)

       elif ms_text == "Сумма":
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          # Задание c
          summa = sum(list)
          bot.send_message(chat_id, f'Сумма: {summa}', reply_markup=markup)

       elif ms_text == "Произведение":
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          # Задание d
          from functools import reduce
          przv = str(reduce(lambda x, y: x*y, list))
          bot.send_message(chat_id, f'Произведение: {przv}', reply_markup=markup)

       elif ms_text == "Факториал":
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          # Задание e
          import math
          bot.send_message(chat_id, text="Факториал какого числа интересует?", reply_markup=markup)

          num = int(input())
          print("Факториал вашего числа", math.factorial(num))
          print()
          bot.send_message(chat_id, f'Произведение: ', reply_markup=markup)






    #Задание a
list = [i for i in range(0, 500) if len(str(i)) == 2 and 10 < i < 20]
print("0/ Лист", list)

    #Задание b
from functools import reduce
print("1/ Максимум списка чисел", reduce(max, list))
print()

    #Задание c
print("2/ Сумма всех чисел списка", sum(list))
print()

    #Задание d
print("3/ Произведение всех чисел списка", reduce(lambda x, y: x*y, list))
print()

    #Задание e
import math
print("4/ Факториал какого числа вас интересует?")
num = int(input())
print("Факториал вашего числа", math.factorial(num))
print()

    #Задание f
import random
import string

print("5/ Какую длину строки хотите увидеть?")
l = int(input())

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))
print("Вот она ваша строка", randStr(N=l))
print()


    #Задание g


    #Задание h
def PascalTriangle(n):
   trow = [1]
   y = [0]
   for x in range(n):
      print(trow)
      trow=[left+right for left,right in zip(trow+y, y+trow)]
   return n>=1

print("6/ Сколько строк треугольника Паскаля требуется?")
nn = int(input())
PascalTriangle(nn)





