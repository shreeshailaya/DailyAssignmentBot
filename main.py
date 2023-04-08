import telegram.ext 
from decouple import config

def start(update, context):
    update.message.reply_text("Hello! Welcome to Daily Assignment BOT")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome to the channel
    """)

Token = config("token")
#print(bot.get_me())
updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
updater.start_polling()
updater.idle()