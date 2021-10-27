# types специальные типы данных что бы мы могли описать анотации в наших функциях
from aiogram import Bot, types
# Dispatcher улавливает действия пользователя и реагирует на то так как мы пропишем
from aiogram.dispatcher import Dispatcher
# executor нужен для того что бы мы могли запустить нашего бота
from aiogram.utils import executor
# из файла auth_data.py заберем токен который будем использовать
from auth_data import token

# Присваеваем нашему боту токен.
bot = Bot(token=token)
# Инициализируем Dispatcher и передаем ему токен.
dp = Dispatcher(bot)

# Создадим дикоратор. Он обозначет события когда в наш чат кто то что то пишет.
@dp.message_handler()
# Запишем функцию которую он дикорирует.
# Сюда будут попадать любые текстовые сообщения для бота которые отправляют пользователи в чат.
async def echo_send(message : types.Message):
    if message.text == "Привет":
        await message.answer("Здарова бро 😉")
    else:
        await message.answer("Поздаровайся бро 😑")
    #await message.answer(message.text)
    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)

# Отправим ответ на сообщения пользователя.
# В данном примере message.text , бот отправит пользователю то что пользователь написал.
# Так же можем использовать if
# Можно сделать 3-мя способами.
# await подождать пока не пояевтся свободное место в потоке данной команды
# message.answer и message.reply, message.reply укажет сообщение на которое отвечает.
# Эти 2 метода позволяют отправить боту сообщения в ответ куда бы не написал пользователь.(группа или личные сообщения)
# await bot.send_message() Данный метод позволяет отправить сообщение непосредственно в личку пользователя.
# Если пользовател напишет в группу где сидит бот но не писал ни разу боту, бот первый пользователю
# написать не сможет в данном случае будет ошибка.
# Он сработает только в том случае если пользователь уже писал боту.
# Что бы написать в личку нужно знать id пользователя. Поэтому в аргумент добавляем
# message.from_user.id таким образом узнаем id


# Запускаем наш бот
# skip_updates=True если не записать то,когда бот не онлайн и ему пользователи будут писать сообщения,
# то когда он выйдет в онлайн, его засыпит сообщениями телеграм сервер и бот будет отвичать.
# skip_updates=True в этом случае бот будет пропускать сообщения которые были переданы ему когда он был.
# не онлайн.
executor.start_polling(dp, skip_updates=True)