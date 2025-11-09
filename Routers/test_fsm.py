from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup

from keyboards.number_guess_keyboard import create_keyboard

fsm_router = Router()


class FSMChooseNumber(StatesGroup):
    guess = State()


@fsm_router.message(
    Command('number', prefix='*'),
    StateFilter(default_state)
)
async def start_number(message: Message, state: FSMContext) -> None:
    await message.reply(
        text=f'state: {await state.get_state()} | start guess number',
        reply_markup=create_keyboard()
    )
    await state.set_state(FSMChooseNumber.guess)


@fsm_router.callback_query(
    F.data.startswith('number_'),
    StateFilter(FSMChooseNumber.guess)
)
async def get_answer(callback: CallbackQuery, state: FSMContext) -> None:
    if callback.message is not None:
        await callback.message.answer(
            text=f'state: {await state.get_state()} | callback: {callback.data}'
        )
    await callback.answer()
    await state.set_state(default_state)