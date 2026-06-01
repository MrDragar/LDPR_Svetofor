import logging

from aiogram import Router, types, filters, F
from aiogram.fsm.context import FSMContext

from src.application.keyboards.menu_keyboard import get_menu_keyboard
from src.application.keyboards.personal_data_keyboard import \
    get_personal_data_keyboard
from src.application.states import RegistrationStates

from src.application.keyboards.miniapp_keyboard import get_miniapp_keyboard
from src.services.interfaces import IUserService

router = Router(name=__name__)
start_command_router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message()
@start_command_router.message(filters.CommandStart())
@start_command_router.message(F.text == 'Отмена')
async def start(message: types.Message, user_service: IUserService,
                state: FSMContext):
    if message.chat.id <= 0:
        return
    await message.reply(
        "Этот бот создан для коммуникации по вопросам формирования баллов показателей: «всероссийского приема граждан» и «агитационная сеть» светофора"
    )
