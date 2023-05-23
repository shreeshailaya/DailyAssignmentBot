import os
import telegram.ext 
from decouple import config
from scraper import soup
from utils import utils
# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential


# keyVaultName = "serects-variables"
# KVUri = f"https://serects-variables.vault.azure.net/"

# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=KVUri, credential=credential)

def start(update, context):
    subjects = list(soup.scrap_subjects())
    subject_removed_list = utils.remove_unwanted_subjects(subjects) 
    updated_list = [item.replace(' ', '_') for item in subject_removed_list]
    formatted_string = "Welcome to Daily AssignmentBOT \n \n SELECT THE SUBJECT \n \n"+'\n'.join([f"/{item}" for item in updated_list])
    update.message.reply_text(formatted_string)
    
def help(update,context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome to the channel
    """)

Token = config("botEnvToken")
#print(Token)
#print(bot.get_me())
updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
updater.start_polling()
updater.idle()
