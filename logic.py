import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text

    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1

        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(
                    option, callback_data="correct"))
            else:
                markup.add(InlineKeyboardButton(option, callback_data="wrong"))
        return markup


quiz_questions = [
    Question("Сколько планет на земле?", 0, "8", "7"),
    Question("В какой стране наибольшее население?",
             1, "Китай", "Индия", "США", "Бразилия"),
    Question("Какая самая молодая страна?", 2,
             "Судан", "Сомали", "Южный Судан")
]
