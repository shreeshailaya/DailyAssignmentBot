import os
import telegram.ext 
from decouple import config
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


keyVaultName = "serects-variables"
KVUri = f"https://serects-variables.vault.azure.net/"

credential = DefaultAzureCredential(connection_verify=False, exclude_shared_token_cache_credential=True)
client = SecretClient(vault_url=KVUri, credential=credential)

def start(update, context):
    update.message.reply_text("Hello! Welcome to Daily Assignment BOT")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome to the channel
    """)

Token = client.get_secret("token")
print(Token)
#print(bot.get_me())
updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
updater.start_polling()
updater.idle()
