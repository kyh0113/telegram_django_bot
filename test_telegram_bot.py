import telegram 

my_token = "6983964934:AAFD4D7FCtRfV5jNEn_n_ZRq6uz-_DVFXj4" 

bot = telegram.Bot(token = my_token)

for update in bot.getUpdates():
    print(update)
    
