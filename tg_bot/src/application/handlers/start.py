import logging

from aiogram import Router, types, filters, F
from aiogram.fsm.context import FSMContext

from src.application.keyboards.menu_keyboard import get_menu_keyboard
from src.application.keyboards.personal_data_keyboard import \
    get_personal_data_keyboard
from src.application.states import RegistrationStates

from src.application.filters import IsRegisteredFilter
from src.domain.entities import Sources
from src.services.interfaces import IUserService

router = Router(name=__name__)
start_command_router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message(IsRegisteredFilter())
async def participant_start(
        message: types.Message,
):
    if message.chat.id <= 0:
        return
    await message.reply(
        "Уважаемые коллеги, данный бот разработан для уведомления о показателях № 2 "
        "«Мобилизационная база» и индикатора № 3 «Вовлеченность депутатов ЛДПР в проведение ВПГ», "
        "показателя № 1 «Выполнение мероприятий планирования» светофора»."
    )


@router.message()
@start_command_router.message(filters.CommandStart())
@start_command_router.message(F.text == 'Отмена')
async def start(message: types.Message,
                state: FSMContext, user_service: IUserService):
    if message.chat.id <= 0:
        return
    if await user_service.exists(message.chat.id, Sources.TG):
        await message.reply(
            "Уважаемые коллеги, данный бот разработан для уведомления о показателях № 2 "
            "«Мобилизационная база» и индикатора № 3 «Вовлеченность депутатов ЛДПР в проведение ВПГ», "
            "показателя № 1 «Выполнение мероприятий планирования» светофора»."
        )
        return
    logging.debug(f"User {message.from_user.id} Start conversation")

    await message.answer_sticker(types.FSInputFile('docs/sokol_stay.webp'))
    await message.reply(
        "Уважаемые коллеги, данный бот разработан для уведомления о показателях № 2 "
        "«Мобилизационная база» и индикатора № 3 «Вовлеченность депутатов ЛДПР в проведение ВПГ», "
        "показателя № 1 «Выполнение мероприятий планирования» светофора»."
    )

    await message.reply(
        "Укажите вашу фамилию"
    )
    await state.set_state(RegistrationStates.surname)