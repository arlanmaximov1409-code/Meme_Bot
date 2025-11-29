@bot.message_handler(commands=['meme'])
def send_mem(message):
    img = random.choice(os.listdir('memes'))
    with open(f'memes/{img}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['cat_memes'])
def send_cat(message):
     img = random.choice(os.listdir('cat_memes'))
     with open(f'cat_memes/{img}', 'rb') as f:
          bot.send_photo(message.chat.id, f)

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)


bot.polling()
