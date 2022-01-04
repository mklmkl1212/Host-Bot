import telebot,random,os,requests
from telebot import types
bot = telebot.TeleBot('#Your Telegram Bot Token!')


# Github: https://github.com/PluginX
# Telegram: https://t.me/Plugin

Max_Files_For_User = 6  # how many user can host bots
Black_Listed_Librarys = ['os', 'base64', 'input', 'bot.py', 'base32', 'marshal',
                         'selenium']  # Black listed lib or words!


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id, text="*Checking if you are in the database* 🕔\nPlease wait..",
                         parse_mode='markdown')
        first = message.chat.first_name

        data = requests.get('https://apis.red/captcha/...hidden...').text

        if str(message.chat.id) in data:
            data2 = requests.get(f'https://apis.red/isVerified/check/?id={message.chat.id}').text
            if 'You Already Have Account On The This IP!' in data2:
                bot.send_message(message.chat.id,
                                 text=f"*Hello* {first}.\nWelcome\n  To the best *Python* host bot\n\n*You are not on the database please open this url so i can add your id on the bot database and make sure the you are not a robot*!\n\nhttps://apis.red/isVerified/check/?id={str(message.chat.id)}\n\nWhen you are done type */start again!*",
                                 parse_mode='markdown')
            else:
                key = types.InlineKeyboardMarkup()
                b1 = types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/Avira')
                b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')

                key.add(b1)
                key.add(b2)

                bot.send_video(message.chat.id, 'https://t.me/thuuu/9',
                               caption=f'*Hello* {first}.\nWelcome\n  To the best *Python* host bot\n\n**Currently version: V0.2**\nMade By: @Plugin\n\n/help\n  *To get the help page*\n\n/files\n  *To get your files*\n\n/info\n  *To see the not allowed libraries*\n\n/get + File ID\n  *To get your file*\n\n/pip + Library name\n  *To install a Library*\n\n/run + Your file Id\n  *To run your bot!*',
                               parse_mode='markdown', reply_markup=key)
        else:
            try:
                bot.send_message(message.chat.id,
                                 text=f"*Hello* {first}.\nWelcome\n  To the best *Python* host bot\n\n*You are not on the database please open this url so i can add your id on the bot database and make sure the you are not a robot*!\n\nhttps://apis.red/isVerified/check/?id={str(message.chat.id)}\n\nWhen you are done type */start again!*",
                                 parse_mode='markdown')
            except:
                bot.send_message(message.chat.id, text="*API is down* 🚫\nPlease contact the coder: @Plugin",
                                 parse_mode='markdown')
    except:
        bot.send_message(message.chat.id, text="*API is down* 🚫\nPlease contact the coder: @Plugin",
                         parse_mode='markdown')


@bot.message_handler(func=lambda m: True)
def Get(message):
    msg = message.text
    first = message.chat.first_name

    try:
        data = requests.get('https://apis.red/captcha/...hidden...').text

        if str(message.chat.id) in data:
            if msg.startswith('/pip'):
                try:

                    data = str(msg).split(' ')
                    the_pip = data[1]

                    if 'telebot' in the_pip:
                        bot.send_message(message.chat.id, text="Installed by the developer ✅")

                    elif 'pyTelegramBotAPI' in the_pip:
                        bot.send_message(message.chat.id, text="Installed by the developer ✅")

                    elif 'requests' in the_pip:
                        bot.send_message(message.chat.id, text="Installed by the developer ✅")

                    else:
                        os.system(f"pip install {the_pip}")
                        bot.send_message(message.chat.id, text="Install success! ✅")

                except:
                    bot.send_message(message.chat.id,
                                     text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start ")

            elif msg.startswith('/run'):
                try:

                    data = str(msg).split(' ')
                    the_file_name = data[1]

                    os.startfile(f"bots\{message.chat.id}\{the_file_name}.py")
                    bot.send_message(message.chat.id, text="Your Bot hosted success! ✅")

                except:
                    bot.send_message(message.chat.id,
                                     text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start ")

            elif msg.startswith('/help'):
                try:

                    key = types.InlineKeyboardMarkup()
                    b1 = types.InlineKeyboardButton(text='Coder', url='https://t.me/Plugin')
                    b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')
                    key.add(b1)
                    key.add(b2)

                    bot.send_photo(message.chat.id, photo='https://t.me/thuuu/8',
                                   caption="*Help Page* 📑\n1- Drag your python file to the bot\n2- Then the bot will give you *File ID*\n\n3- Then install your Librarys\n 🔍 using /pip + *library name*\n\n4- Run your bot\n 🔍 using /run + *File iD*\n\n*Contact*: @Plugin",
                                   parse_mode='markdown', reply_markup=key)

                except:
                    bot.send_message(message.chat.id,
                                     text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start ")

            elif msg.startswith('/files'):
                try:

                    key = types.InlineKeyboardMarkup()
                    b1 = types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/Avira')
                    b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')
                    key.add(b1)
                    key.add(b2)

                    files = os.listdir(f'bots/{message.chat.id}')
                    lenFiles = len(files)
                    msgfile = '''┌ Your Files\n'''
                    for i in range(lenFiles):
                        msgfile += '├ ' + files[i].split('.')[0] + '\n'

                    msgfile += '└ ' + f'ID: {message.chat.id}' + '\n'

                    bot.send_message(message.chat.id,text=msgfile,
                                   parse_mode='markdown', reply_markup=key)

                except:
                    bot.send_message(message.chat.id,
                                     text=f"Sorry you dont have files yet!")

            elif msg.startswith('/info'):
                try:

                    key = types.InlineKeyboardMarkup()
                    b1 = types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/Avira')
                    b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')
                    key.add(b1)
                    key.add(b2)

                    msgfile = '''┌ *Not allowed*\n'''
                    for i in Black_Listed_Librarys:
                        msgfile += '├ ' + i.title() + '\n'

                    msgfile += '└ ' + f'ID: {message.chat.id}' + '\n'

                    bot.send_message(message.chat.id,text=msgfile,
                                   parse_mode='markdown', reply_markup=key)

                except:
                    bot.send_message(message.chat.id,
                                     text=f"Sorry you don't have files yet!")

            elif msg.startswith('/get'):
                try:

                    data = str(msg).split(' ')
                    the_file_name = data[1]
                    with open(f'bots/{message.chat.id}/{the_file_name}.py','rb') as readbytes:
                        rdr = readbytes.read()
                    readbytes.close()
                    bot.send_document(message.chat.id,rdr,)

                except:
                    bot.send_message(message.chat.id,text=f"Sorry you don't have that file!")

            else:
                bot.send_message(message.chat.id, text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start")



        else:
            try:
                bot.send_message(message.chat.id,
                                 text=f"*Hello* {first}.\nWelcome\n  To the best *Python* host bot\n\n*You are not on the database please open this url so i can add your id on the bot database and make sure the you are not a robot*!\n\nhttps://apis.red/isVerified/check/?id={str(message.chat.id)}\n\nWhen you are done type */start again!*",
                                 parse_mode='markdown')
            except:
                bot.send_message(message.chat.id, text="*API is down* 🚫\nPlease contact the coder: @Plugin",
                                 parse_mode='markdown')
    except:
        bot.send_message(message.chat.id, text="*API is down* 🚫\nPlease contact the coder: @Plugin",
                         parse_mode='markdown')


@bot.message_handler(content_types=['document'])
def save(message):
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    ran = 'a' + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(
        chars) + random.choice(chars) + random.choice(chars) + random.choice(chars)

    try:
        os.makedirs('bots/' + str(message.chat.id) + '/')
    except:
        pass
    with open('bots/' + str(message.chat.id) + '/' + ran + '.py', 'wb') as new_file:
        new_file.write(downloaded_file)

    getLen = len(os.listdir('bots/' + str(message.chat.id) + '/'))

    if int(getLen) >= int(Max_Files_For_User + 1):
        bot.send_message(message.chat.id, text=f'*You have upload {getLen} files\n You cant upload more* 🚫',
                         parse_mode='markdown')
        os.remove('bots/' + str(message.chat.id) + '/' + ran + '.py')
    else:
        try:
            BlackListedLib = ''
            emptystr = False
            for i in Black_Listed_Librarys:
                search = str(downloaded_file).find(i)
                if search > 0:
                    emptystr = True
                    BlackListedLib += i
                    break

            if BlackListedLib == 'os':
                search = str(downloaded_file).find('post')
                if search > 0:
                    emptystr = False

            if emptystr == True:
                bot.reply_to(message, text=f'You cant use *{BlackListedLib}* 🚫\nFile Removed! ', parse_mode='markdown')
                os.remove('bots/' + str(message.chat.id) + '/' + ran + '.py')
            else:
                bot.send_message(message.chat.id, text=f'*File upload success* ✅\n*Your File ID*:',
                                 parse_mode='markdown')
                bot.send_message(message.chat.id, text=f'```{ran}```', parse_mode='markdown')
        except:
            bot.send_message(message.chat.id,
                             text=f'*Error in file upload contact the coder* 🚫\nPlease try again later',
                             parse_mode='markdown')


bot.polling(True)
