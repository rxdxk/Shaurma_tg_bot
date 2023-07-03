from telebot import types

start_kb = types.InlineKeyboardMarkup()
butn1 = types.InlineKeyboardButton("Наша адреса",url=r'https://www.google.com/maps/place/%D1%83%D0%BB.+%D0%90%D0%BD%D0%BD%D1%8B+%D0%90%D1%85%D0%BC%D0%B0%D1%82%D0%BE%D0%B2%D0%BE%D0%B9,+1,+%D0%9A%D0%B8%D0%B5%D0%B2,+02000/@50.4128532,30.6407127,17z/data=!3m1!4b1!4m6!3m5!1s0x40d4c5015f137b37:0xaf22765b5226e0a9!8m2!3d50.4128498!4d30.6432876!16s%2Fg%2F11lpc_7s3p?authuser=0&entry=ttu')
start_kb.add(butn1)

main_menu_buttons = [types.KeyboardButton("Контакти"),
                     types.KeyboardButton("Меню")]
main_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*main_menu_buttons)
