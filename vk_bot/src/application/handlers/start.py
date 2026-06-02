import logging
from vkbottle.bot import BotLabeler, Message
from vkbottle import PhotoMessageUploader
from vkbottle.dispatch import BuiltinStateDispenser

from src.application.states import RegistrationStates
from src.services.interfaces import IUserService

router = BotLabeler()
start_command_router = BotLabeler()
logger = logging.getLogger(__name__)


@router.message()
@start_command_router.message(text=["Начать", "/start", "start", "начать", "Заново", "заново"])
async def start(
        message: Message, user_service: IUserService, 
        state_dispenser: BuiltinStateDispenser, photo_uploader: PhotoMessageUploader,
):
    if message.peer_id < 0:
        return
    try:
        await state_dispenser.delete(message.from_id)
    except:
        ...
    if await user_service.is_user_exists(message.from_id):
        await message.answer(
            "Этот бот создан для коммуникации по вопросам формирования баллов показателей: «всероссийского приема граждан» и «агитационная сеть» светофора")
        return

    photo = await photo_uploader.upload('docs/sokol_stay.webp', peer_id=message.peer_id)
    await message.answer(attachment=photo)
    await message.answer("Этот бот создан для коммуникации по вопросам формирования баллов показателей: «всероссийского приема граждан» и «агитационная сеть» светофора")
    await state_dispenser.set(message.from_id, RegistrationStates.SURNAME)
    await message.reply(
        "Укажите вашу фамилию"
    )
