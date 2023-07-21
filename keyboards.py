from telebot import types 
#Стартовая инлайн клавиатура с адресом рестрорана
start_kb = types.InlineKeyboardMarkup()
butn1 = types.InlineKeyboardButton("Наша адреса",url=r'https://www.google.com/maps/place/%D1%83%D0%BB.+%D0%90%D0%BD%D0%BD%D1%8B+%D0%90%D1%85%D0%BC%D0%B0%D1%82%D0%BE%D0%B2%D0%BE%D0%B9,+1,+%D0%9A%D0%B8%D0%B5%D0%B2,+02000/@50.4128532,30.6407127,17z/data=!3m1!4b1!4m6!3m5!1s0x40d4c5015f137b37:0xaf22765b5226e0a9!8m2!3d50.4128498!4d30.6432876!16s%2Fg%2F11lpc_7s3p?authuser=0&entry=ttu')
start_kb.add(butn1)

def fill_in_keyboard(keyboard_positions,keyboard_buttons,is_keyboard_inline = False):
    if is_keyboard_inline == False:
        for x in keyboard_positions:
          keyboard_buttons.append(types.KeyboardButton(x))
    else:
       for x in keyboard_positions:
          keyboard_buttons.append(types.InlineKeyboardButton(x,callback_data=x))
#Клавиатура да/нет
yes_or_no_buttons = [types.KeyboardButton('Так✅'),
                     types.KeyboardButton('Ні❌')]
yes_or_no_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*yes_or_no_buttons)
#Клавиатура главного меню
main_menu_buttons = [types.KeyboardButton("Меню📋"),
                     types.KeyboardButton("Оформити замовлення✍️"),]
main_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*main_menu_buttons)
#Клавиатура заказа
order_positions = ["Шаурма🌯","Фалафель🧆","Роли🌯","Гарніри🍟","Напої🥤","Додатки",]
order_buttons = []
fill_in_keyboard(order_positions,order_buttons,True)
order_kb = types.InlineKeyboardMarkup().add(*order_buttons)
#Клавиатура позиций шаурмы
shaurma_posititons = ['Міні патч🤏',"Стандартний патч🫴","Середній патч🤚","Подвійний патч🫲🫱","Shaurma island🧭","Shaurma imba💪","Jalapeno island🌶","Назад🔙","Завершити замовленя⛔️"]
shaurma_buttons = []
fill_in_keyboard(shaurma_posititons,shaurma_buttons)
shaurma_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*shaurma_buttons)
#Клавиатура позиций фалаелей
falafel_positions = ["Наршараб","Чеддерна в піті🧀","Назад🔙","Завершити замовленя⛔️"]
falafel_buttons = []
fill_in_keyboard(falafel_positions,falafel_buttons)
falafel_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*falafel_buttons)
#Клавиатура позиций гарниров 
garniers_positions = ["Box фрі🍟","Box по-селянськи🥔","По-селянськи🥔","Нагетси🐓","Назад🔙","Завершити замовленя⛔️"]
garniers_buttons = []
fill_in_keyboard(garniers_positions,garniers_buttons)
garniers_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*garniers_buttons)
#Клавиатура позиций ролов
rols_positions = ["Фалафель рол🧆","Французький рол🇫🇷","Баварський рол🇩🇪","Подвійний рол баварський🇩🇪🇩🇪","Подвійний рол французький🇫🇷🇫🇷","Назад🔙","Завершити замовленя⛔️"]
rols_buttons = []
fill_in_keyboard(rols_positions,rols_buttons)
rols_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*rols_buttons)
#Клавиатура позиций напитков
drinks_positions = ["Coca-cola🥤","Sprite🍋","Fanta🍊","Назад🔙","Завершити замовленя⛔️"]
drinks_buttons=  []
fill_in_keyboard(drinks_positions,drinks_buttons)
drinks_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*drinks_buttons)

order_buttons_list = [*shaurma_posititons,*rols_positions,*drinks_positions,*falafel_positions,*garniers_positions]
