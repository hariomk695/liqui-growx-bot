import requests
import time
from telegram import Bot

TELEGRAM_BOT_TOKEN = '7919022754:AAE5aabOgAFC0gZ9MjVEbMe-pmO53OuFto0'
TELEGRAM_CHAT_ID = '5619360782'
BITGET_API_KEY = 'bg_c08bedae8a63ac89279381540cfb5cf2'
BITGET_SECRET = 'e986027a9208f76dcee431aa8e6bf640b9e2bf6015ea6d372021d10e5671a4cd'
BITGET_PASSPHRASE = 'Jeet12345'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def get_balance():
    try:
        # Replace this with real Bitget balance logic
        return {"USDT": 100.25}
    except Exception as e:
        print("Error fetching balance:", e)
        return None

def notify_telegram(message):
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print("Telegram Error:", e)

def main_loop():
    while True:
        balance = get_balance()
        if balance:
            notify_telegram(f"Current Wallet Balance:\nUSDT: {balance['USDT']}")
        time.sleep(3600)  # 60 minutes

if __name__ == '__main__':
    main_loop()
