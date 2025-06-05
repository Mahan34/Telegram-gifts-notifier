from telethon.sync import TelegramClient

# اطلاعات ورود
api_id = 25343822
api_hash = 'bfd8f4e1b8e27a232694ef625ab64d36'
phone_number = '+393899983860'  # شماره‌ت رو اینجا گذاشتی

# ساخت کلاینت
client = TelegramClient('session_name', api_id, api_hash)

# ورود به حساب کاربری
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    code = input('کد تأیید ارسال‌شده به تلگرام را وارد کن: ')
    client.sign_in(phone_number, code)

print("✅ ورود با موفقیت انجام شد!")

client.disconnect()