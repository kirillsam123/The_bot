from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = [
    [
        InlineKeyboardButton(text="1", callback_data="number_1"),
        InlineKeyboardButton(text="2", callback_data="number_2")
    ],
    [
        InlineKeyboardButton(text="3", callback_data="number_3"),
        InlineKeyboardButton(text="4", callback_data="number_4")
    ],
    [
        InlineKeyboardButton(text="5", callback_data="number_5"),
        InlineKeyboardButton(text="6", callback_data="number_6")
    ]
]


def create_keyboard() ->  InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=keyboard)