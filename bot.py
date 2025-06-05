import configparser
import time
from telethon import TelegramClient, events
import asyncio

# خواندن تنظیمات از config.ini
config = configparser.ConfigParser()
config.read('config.ini')

api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']
channel_id = config['Telegram']['channel_id']  # شناسه کانال برای ارسال نوتیفیکیشن
check_interval = int(config['Settings']['check_interval'])  # مثلا هر 600 ثانیه (10 دقیقه)

client = TelegramClient('session_name', api_id, api_hash)

last_gift_id = None

async def check_gifts():
    global last_gift_id
    while True:
        # TODO: این قسمت باید کد چک کردن گیفت جدید رو بنویسیم
        # فعلا فرض می‌کنیم یک تابع get_latest_gift() وجود داره که آخرین گیفت رو میده

        latest_gift = await get_latest_gift()

        if latest_gift and latest_gift != last_gift_id:
            last_gift_id = latest_gift
            message = f"🎁 گیفت جدید منتشر شد! شناسه گیفت: {latest_gift}"
            await client.send_message(int(channel_id), message)

        await asyncio.sleep(check_interval)

async def get_latest_gift():
    # این تابع باید مکانیزم بررسی گیفت جدید توی قسمت send a gift تلگرام رو پیاده کنه
    # چون API عمومی تلگرام برای این بخش نیست، باید روش دیگه‌ای پیدا کنیم یا با اسکرین‌شات و ... (پیچیده)
    # اینجا صرفا نمونه فرضی گذاشته شده.
    return "gift_12345"

async def main():
    await client.start()
    print("ربات شروع به کار کرد...")
    await check_gifts()

with client:
    client.loop.run_until_complete(main())