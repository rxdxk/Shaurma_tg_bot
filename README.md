# Shaurma Island — Telegram ordering bot 🌯

Telegram bot for a street-food spot: customers browse the menu, build a basket and place an order,
and the order lands in the staff group chat automatically.

## Features
- `/start` greeting with photo and a button with the restaurant's location on Google Maps
- Menu with reply / inline keyboards generated from a config
- Per-user basket kept in memory during the session
- Checkout flow: phone number + delivery address
- Orders saved to SQLite and forwarded to the staff group chat
- `/help` with usage hints

## Run
```bash
pip install pyTelegramBotAPI python-dotenv
cp .env.sample .env    # API_TOKEN, group_chat_id
python main.py
```

## Structure
```
main.py            entry point (polling)
config.py          bot instance, env loading
commands.py        /start, /help
message.py         menu & checkout messages
callback.py        inline button callbacks
send_photo_func.py photo helper
keyboards.py       menu & inline keyboards
db.py              SQLite orders + forwarding to staff chat
```

## Stack
Python · pyTelegramBotAPI · SQLite · python-dotenv
