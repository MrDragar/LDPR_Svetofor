from aiogram import types
from aiogram.fsm.context import FSMContext

from src.services.interfaces import IUserService


async def finish_registration(user_service: IUserService, state: FSMContext, message: types.Message, log_chat: str):
    data = await state.get_data()
    surname = data['surname']
    name = data['name']
    patronymic = data['patronymic']
    region = data['region']
    if await user_service.is_user_exists(message.chat.id):
        try:
            await state.clear()
        except:
            ...
        return await message.reply(f"Вы уже зарегистрировались.")

    user = await user_service.create_user(
        message.chat.id,
        surname, name, patronymic, region
    )

    await message.answer_sticker(
        types.FSInputFile('docs/sokol_like.webp')
    )
    await message.answer(
        f"Поздравляем, вы успешно зарегистрированы.\n",
        parse_mode="HTML",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await message.bot.send_message(chat_id=log_chat, text=f"""
Новый пользователь 
{'@' + message.chat.username if message.chat.username else '<нет username>'} 
зарегистрировался.
Источник: ТГ
ФИО: {user.surname} {user.name} {user.patronymic}
Регион: {user.region}

ID: {user.id}
""")




