from aiogram import Bot, types, Dispatcher, executor
import logging
from config import TOKEN, html
import parser as ps
import time
import random
import os
import qrcode

def make_qr(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    img_qr = qr.make_image(fill_color='white', back_color="black")
    img_qr.save('qr.png')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    print('Бот онлайн')
    
@dp.message_handler(commands='numhent')
async def numhent(msg : types.Message):
    number = msg.text.split(' ', 1)
    try:       
        ps.get_html(html,number[1])
        photo = ps.parse('content', number[1])
        await msg.reply_photo(photo,caption=number[1])
    except:
        await msg.reply('отправь число дурак')

@dp.message_handler(commands='hent')
async def hent(msg : types.Message):
    rnd = random.randint(1,6330000)
    ps.get_html(html,rnd)
    t = ps.parse('content', rnd)
    await msg.reply_photo(t,caption=rnd)

@dp.message_handler(commands='qr')
async def test(msg : types.Message):
    split = msg.text.split(' ', 1)[1]
    make_qr(split)
    await msg.reply_photo(open('qr.png', 'rb'), caption=split)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True, on_startup=on_startup)
