
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

def Bot():
    token = "YOUR_TELEGRAM_BOT_TOKEN"
    bot = telegram.Bot(token=token)

    # Check for new error messages
    with open('error_log.txt', 'r') as f:
        error_messages = f.readlines()

    # If new errors exist, send them to the Telegram channel
    for error_msg in error_messages:
        bot.send_message(chat_id='YOUR_CHANNEL_OR_USER_ID', text=error_msg)

    # Clear the error log
    with open('error_log.txt', 'w') as f:
        f.truncate()

scheduler = BlockingScheduler()
scheduler.add_job(Bot, 'interval', seconds=600)
scheduler.start()
