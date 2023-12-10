from collections import defaultdict

import telebot

from config import token
from logic import quiz_questions

user_responses = {}
points = defaultdict(int)
bot = telebot.TeleBot(token)


def send_question(chat_id):
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text,
                     reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "correct":
        bot.answer_callback_query(call.id,  "Ответ верный! ✅")
    else:
        bot.answer_callback_query(call.id, "Ответ неверный! ❌")

    user_responses[call.message.chat.id] += 1

    if user_responses[call.message.chat.id] >= len(quiz_questions):
        bot.send_message(call.message.chat.id,
                         f"Квиз завершен, Вы справились! ⚡️\nКоличество очков: {points['user']}")
    else:
        send_question(call.message.chat.id)


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)
    else:
        bot.send_message(message.chat.id, "Вы ответили на все вопросы! 😼")


bot.infinity_polling()
