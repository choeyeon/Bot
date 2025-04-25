import pandas as pd
import matplotlib.pyplot as plt
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("Надішліть мені CSV-файл, і я проаналізую його!")

def analyze_csv(update, context):
    # Отримуємо файл від користувача
    file = update.message.document.get_file()
    file.download('user_data.csv')
    
    # Аналіз даних
    df = pd.read_csv('user_data.csv')
    summary = df.describe().to_markdown()
    
    # Візуалізація
    df.plot(kind='hist')
    plt.savefig('chart.png')
    
    # Відправляємо результат
    update.message.reply_markdown(f"```\n{summary}\n```")
    update.message.reply_photo(photo=InputFile('chart.png'))

# Запуск бота
updater = Updater("7148142766:AAG8uTQSEPL8Dk30xcy-6h5mHc2QD3Lr6bI", use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.document, analyze_csv))
updater.start_polling()