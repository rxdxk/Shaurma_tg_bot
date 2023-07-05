from telebot import types 
#Стартовая инлайн клавиатура с адресом рестрорана
start_kb = types.InlineKeyboardMarkup()
butn1 = types.InlineKeyboardButton("Наша адреса",url=r'https://www.google.com/maps/place/%D1%83%D0%BB.+%D0%90%D0%BD%D0%BD%D1%8B+%D0%90%D1%85%D0%BC%D0%B0%D1%82%D0%BE%D0%B2%D0%BE%D0%B9,+1,+%D0%9A%D0%B8%D0%B5%D0%B2,+02000/@50.4128532,30.6407127,17z/data=!3m1!4b1!4m6!3m5!1s0x40d4c5015f137b37:0xaf22765b5226e0a9!8m2!3d50.4128498!4d30.6432876!16s%2Fg%2F11lpc_7s3p?authuser=0&entry=ttu')
start_kb.add(butn1)

#Клавиатура да/нет
yes_or_no_buttons = [types.KeyboardButton('Так'),
                     types.KeyboardButton('Ні')]
yes_or_no_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*yes_or_no_buttons)



#Клавиатура главного меню
main_menu_buttons = [types.KeyboardButton("Меню"),
                     types.KeyboardButton("Зробити замовлення"),]
main_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*main_menu_buttons)

#Клавиатура заказа
order_buttons = [types.InlineKeyboardButton("Шаурма",callback_data='Шаурма'),
            types.InlineKeyboardButton("Фалафель",callback_data="Фалафель"),
            types.InlineKeyboardButton("Роли",callback_data="Роли"),
            types.InlineKeyboardButton("Гарніри",callback_data="Гарніри"),
            types.InlineKeyboardButton("Напої",callback_data="Напої"),
            types.InlineKeyboardButton("Додатки",callback_data="Додатки")]
order_kb = types.InlineKeyboardMarkup().add(*order_buttons)



#Клавиатура позиций шаурмы
shaurma_posititons = ['Міні патч',"Стандартний патч","Середній патч","Подвійний патч","Shaurma island","Shaurma imba","Jalapeno island","Назад","Завершити замовленя"]
shaurma_buttons = [types.KeyboardButton(shaurma_posititons[0]),
                   types.KeyboardButton(shaurma_posititons[1]),
                   types.KeyboardButton(shaurma_posititons[2]),
                   types.KeyboardButton(shaurma_posititons[3]),
                   types.KeyboardButton(shaurma_posititons[4]),
                   types.KeyboardButton(shaurma_posititons[5]),
                   types.KeyboardButton(shaurma_posititons[6]),
                   types.KeyboardButton(shaurma_posititons[7]),
                   types.KeyboardButton(shaurma_posititons[8])]

shaurma_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*shaurma_buttons)


#Клавиатура позиций фалаелей
falafel_positions = ["Наршараб","Чеддерна в піті","Назад","Завершити замовленя"]
falafel_buttons = [types.KeyboardButton(falafel_positions[0]),
                   types.KeyboardButton(falafel_positions[1]),
                   types.KeyboardButton(falafel_positions[2]),
                   types.KeyboardButton(falafel_positions[3]),]

falafel_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*falafel_buttons)


#Клавиатура позиций гарниров 
garniers_positions = ["Box фрі","Box по-селянськи","По-селянськи","Нагетси","Назад","Завершити замовленя"]
garniers_buttons = [types.KeyboardButton(garniers_positions[0]),
                types.KeyboardButton(garniers_positions[1]),
                types.KeyboardButton(garniers_positions[2]),
                types.KeyboardButton(garniers_positions[3]),
                types.KeyboardButton(garniers_positions[4]),
                types.KeyboardButton(garniers_positions[5]),]

garniers_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*garniers_buttons)


#Клавиатура позиций ролов
rols_positions = ["Фалафель рол","Французький рол","Баварський рол","Подвійний рол баварський","Продівйний рол французький","Назад","Завершити замовленя"]
rols_buttons = [types.KeyboardButton(rols_positions[0]),
                types.KeyboardButton(rols_positions[1]),
                types.KeyboardButton(rols_positions[2]),
                types.KeyboardButton(rols_positions[3]),
                types.KeyboardButton(rols_positions[4]),
                types.KeyboardButton(rols_positions[5]),
                types.KeyboardButton(rols_positions[6]),]

rols_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*rols_buttons)


#Клавиатура позиций напитков
drinks_positions = ["Coca-cola","Sprite","Fanta","Назад","Завершити замовленя"]
drinks_buttons=  [types.KeyboardButton(drinks_positions[0]),
                  types.KeyboardButton(drinks_positions[1]),
                  types.KeyboardButton(drinks_positions[2]),
                  types.KeyboardButton(drinks_positions[3]),
                  types.KeyboardButton(drinks_positions[4]),]


drinks_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*drinks_buttons)

#Клавиатура позиций добавлений
dodatki_positions = ["Кукурудза","Чеддерний соус","Соус Наршараб","Сир Ананас","Перець Халапеньо","Картопля","Завершити замовленя"]
dodatki_buttons = [types.KeyboardButton(dodatki_positions[0]),
                   types.KeyboardButton(dodatki_positions[1]),
                   types.KeyboardButton(dodatki_positions[2]),
                   types.KeyboardButton(dodatki_positions[3]),
                   types.KeyboardButton(dodatki_positions[4]),
                   types.KeyboardButton(dodatki_positions[5]),
                   types.KeyboardButton(dodatki_positions[6]),]
dodatki_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*dodatki_buttons)
