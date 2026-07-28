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
            "Уважаемые коллеги!\n\n"
            "С целью оперативного информирования и направления актуальных материалов был разработан "
            "данный чат-бот для кураторов БКЛ (организационный менеджер по полевой и сетевой работе)."
        )
        return

    photo = await photo_uploader.upload('docs/sokol_stay.webp', peer_id=message.peer_id)
    await message.answer(attachment=photo)
    await message.answer("Уважаемые коллеги, данный бот разработан для уведомления о показателях № 2 «Мобилизационная база» и индикатора № 3 «Вовлеченность депутатов ЛДПР в проведение ВПГ», показателя № 1 «Выполнение мероприятий планирования» светофора")
    await state_dispenser.set(message.from_id, RegistrationStates.SURNAME)
    await message.reply(
        "Укажите вашу фамилию"
    )
