from api import get_categories, get_products
from keyboards import create_category_keyboard,remove_keyboard,main_markup
from db import Query

temp_data = {}

def low_controller(message, bot):
    bot.send_message(
        message.chat.id,
        "Вы выбрали фильтрацию по убыванию. Выберите одну из категорий",
        reply_markup = create_category_keyboard(get_categories())
    )



    temp_data[message.chat.id] = {'type':message.text}

    bot.register_next_step_handler(message, lambda m: category_controller(m, bot))


def category_controller(message, bot):
    bot.send_message(
        message.chat.id,
        "Отлично! Категория для фильтрации выбрана. Укажите количество результатов для получения.",
        reply_markup = remove_keyboard()
    )
    temp_data[message.chat.id]['category'] = message.text
    bot.register_next_step_handler(message, lambda m: amount_controller(m, bot))


def amount_controller(message, bot):
    temp_data[message.chat.id]['amount'] = message.text
    bot.send_message(
        message.chat.id,
        f"Выборка из {message.text} товаров",
        reply_markup = main_markup()
    )
    sorted_products = sorted(get_products(temp_data[message.chat.id]['category']), key=lambda x: x['price'])[:int(temp_data[message.chat.id]['amount'])]
    for i in sorted_products:
        bot.send_message(
            message.chat.id,
            f"{i['title']} | {i['price']}"
        )

    Query(
        chat_id=message.chat.id,
        type=temp_data[message.chat.id]['type'],
        category=temp_data[message.chat.id]['category'],
        amount=int(temp_data[message.chat.id]['amount'])
    ).save()
    temp_data.pop(message.chat.id)