import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '********************************'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Hi!\nSend me message or file and i'll resend it to you.\nSupported: text, photo, document, video, "
        "animation, audio, voice.")


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(content_types=['photo'])
async def scan_message(msg: types.Message):
    await msg.answer_photo(msg.photo[0].file_id)


@dp.message_handler(content_types=['document'])
async def scan_doc(msg: types.Message):
    await msg.answer_document(msg.document.file_id)


@dp.message_handler(content_types=['video'])
async def scan_doc(msg: types.Message):
    await msg.answer_video(msg.video.file_id)


@dp.message_handler(content_types=['audio'])
async def scan_doc(msg: types.Message):
    await msg.answer_audio(msg.audio.file_id)


@dp.message_handler(content_types=['voice'])
async def scan_doc(msg: types.Message):
    await msg.answer_voice(msg.voice.file_id)


@dp.message_handler(content_types=['animation'])
async def scan_doc(msg: types.Message):
    await msg.answer_animation(msg.animation.file_id)


if __name__ == '__main__':
    print('by Santiagz : https://github.com/santiagz')
    executor.start_polling(dp, skip_updates=True)
