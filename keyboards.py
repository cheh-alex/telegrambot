from telebot.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

def create_category_keyboard(categories):
    k = ReplyKeyboardMarkup()
    for i in categories:
        k.row((KeyboardButton(i)))
    return k

def remove_keyboard():
    return ReplyKeyboardRemove()


def main_markup():
    k = ReplyKeyboardMarkup()
    k.row(KeyboardButton('/low'))
    k.row(KeyboardButton('/high'))
    k.row(KeyboardButton('/custom'))
    k.row(KeyboardButton('/history'))
    return k