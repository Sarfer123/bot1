import logging 
from aiogram import Bot, Dispatcher, executor, types
import markup as nav

TOKEN = '5270779486:AAGnW8qUvOJz6Y0oqxmqlK93Yx_rWp4jYxs'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id, """Привет, {0.first_name}👋 
Чем я могу тебе помочь?""".format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
	if message.text == '🎯 Тренировки':
		await bot.send_message(message.from_user.id, '🎯 Тренировки', reply_markup = nav.otherMenu)
	
	elif message.text == '🔙Назад':
		await bot.send_message(message.from_user.id, '🔙Назад', reply_markup = nav.mainMenu)

	elif message.text == '✅Консультации':
		await bot.send_message(message.from_user.id, '✅Консультации', reply_markup = nav.otherMeny)
	
	elif message.text == '🚀 Обо мне':
		await bot.send_message(message.from_user.id, """Привет👋 Меня зовут Алекс.
Я выступающий спортсмен NPC в категории men's physique & classic physique.
Дипломированный специалист в области фитнеса.""")

	elif message.text == '🏅Персональная тренировка':
		await bot.send_message(message.from_user.id, """🎯 Персональная тренировка в зале - 1 час
✅Стоимость:

1 тренировка 3000₽

10 тренировок 25000₽""")

	elif message.text == '🖥Онлайн-ведение':
		await bot.send_message(message.from_user.id, """🎯 Онлайн ведение

✅Стоимость: 10000₽ в месяц

1. Индивидуальная программа тренировок
2. Контроль результатов и связь 24/7
3. Рекомендации по спортивным добавкам
4. Расчёт БЖУ и составление схемы питания
5. 3 личные тренировки в зале""")

	elif message.text == '🖥Онлайн-ведение':
		await bot.send_message(message.from_user.id, """🎯 Составление программы тренировок

✅Стоимость: 10000₽

1. Составление программы тренировок
2. Проработка программы тренировок в зале""")

	elif message.text == '🏋️Программа тренировок':
		await bot.send_message(message.from_user.id, """🎯 Составление программы тренировок

✅Стоимость: 10000₽

1. Составление программы тренировок
2. Проработка программы тренировок в зале""")


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)
