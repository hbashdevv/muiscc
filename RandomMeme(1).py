import requests
from telebot import types
import telebot
from time import sleep
import random
token = input(" [~] Enter Token : ")
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="- الحصول",callback_data = 'check')
#----#


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
اهلا بك في بوت  اغنية او ميمز عشوائي 
اضغط الحصول لجلب ميمز او اغنية عشوائي
- - - - - - - - - - 
By  : @trprogram 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	combo(call.message)   	
def combo(message):
		bot.send_message(message.chat.id,"<strong>يتم العثور الرجاء الانتظار... </strong>",parse_mode="html")
		rl = random.randint(1,1000)
		url = f"https://t.me/fasngon/{rl}"
		bot.send_audio(message.chat.id,url,caption="<strong>تم العثور 😂</strong>",parse_mode="html")
		
    
pass
#داشوفك تريد تخمط
bot.polling(True)