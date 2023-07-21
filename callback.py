from config import bot
import keyboards

callback_data_handlers = {
    "Шаурма🌯": keyboards.shaurma_kb,
    "Фалафель🧆": keyboards.falafel_kb,
    "Гарніри🍟": keyboards.garniers_kb,
    "Роли🌯": keyboards.rols_kb,
    "Напої🥤": keyboards.drinks_kb
}

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    data = callback.data
    if data in callback_data_handlers:
        keyboard = callback_data_handlers[data]
        bot.send_message(callback.message.chat.id, f"Це наші {data.lower()}", reply_markup=keyboard)



    
