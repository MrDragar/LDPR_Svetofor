import logging
from vkbottle.bot import BotLabeler, Message
from vkbottle import PhotoMessageUploader
from vkbottle.dispatch import BuiltinStateDispenser

from src.application.keyboards.personal_data_keyboard import get_personal_data_keyboard
from src.application.keyboards.miniapp_keyboard import get_miniapp_keyboard
from src.application.states import RegistrationStates
from src.services.interfaces import IUserService

router = BotLabeler()
start_command_router = BotLabeler()
logger = logging.getLogger(__name__)


@router.message()
@start_command_router.message(text=["Начать", "/start", "start", "начать", "Заново", "заново"])
async def start(
        message: Message, user_service: IUserService, 
        state_dispenser: BuiltinStateDispenser, photo_uploader: PhotoMessageUploader
):
    if message.peer_id < 0:
        return
    await message.answer("Этот бот создан для коммуникации по вопросам формирования баллов показателей: «всероссийского приема граждан» и «агитационная сеть» светофора")
