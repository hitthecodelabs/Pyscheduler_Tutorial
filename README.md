
# Automated Error Handling with Telegram Alerts

The purpose of this guide is to demonstrate an efficient method for logging errors and notifying developers via Telegram when an error occurs. This method uses the `apscheduler` library to periodically check for updates in the error log and sends notifications using the `python-telegram-bot` library.

## Prerequisites

1. Python 3.x installed.
2. `apscheduler` library installed.
3. `python-telegram-bot` library installed.
4. A Telegram Bot Token and a channel ID (or user ID) to send messages.

## Steps:

1. **Error Logging**:
   Whenever an error occurs in your code, catch the exception and save the detailed error message into a `.txt` file.

```python
import sys
import traceback

try:
    ### code
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    error_l = exc_tb.tb_lineno
    cadena_error = str(exc_type) + " => " + str(exc_obj)
    error_info = traceback.format_exc()

    # Append the error details to the error_log.txt
    with open('error_log.txt', 'a') as f:
        f.write(cadena_error + "\n" + error_info + "\n\n")
```

2. **Initialize the Telegram Bot**:
   Define a function to send messages using the Telegram Bot. Replace `token`, `chat_id`, and other parameters with your own.

```python
import telegram

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
```

## How to Find the Telegram Channel ID

To find the ID of a Telegram channel (or group/user):

1. Start a conversation with your bot or add it to the desired channel.
2. Visit the following URL in your browser:

```
https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/getupdates
```

Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual bot token.

3. In the resulting JSON output, locate the `chat` object. The `id` inside this object is the channel ID. It will look something like this:

```json
"chat": {
    "id": -1101845415028,
    ...
}
```

4. Use this `id` as the `chat_id` in your code.

3. **Schedule the Bot to Run Periodically**:
   Use `apscheduler` to run the `Bot` function every 10 minutes (or 600 seconds).

```python
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(Bot, 'interval', seconds=600)
scheduler.start()
```

## Running the Code

1. Replace placeholders like `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_CHANNEL_OR_USER_ID` with your actual values.
2. Save the combined code in a Python script, e.g., `error_handler.py`.
3. Run the script using the command: `python error_handler.py`.

## Conclusion

This setup allows for automated error logging and instant notifications via Telegram. It's an efficient way to stay updated on issues that might arise in your application and resolve them promptly. 

