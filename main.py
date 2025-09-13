from aiogram import Bot, Dispatcher, Router, types
import asyncio
from aiogram.types import FSInputFile
from config import TOKEN
from aiogram.filters import Command
from aiogram.fsm.state  import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import create_keyboard
from Service.database import info_retrieve

bot = Bot(TOKEN)
dp = Dispatcher()
rg = Router()

class States(StatesGroup):
    start_menu = State()
    start_fill_form = State()

@rg.message(Command("start"))
async def start(message:types.Message, state:FSMContext):
    await state.set_state(States.start_menu)
    info = info_retrieve()[0]
    text, image_name = info[1], info[3]
    photo = FSInputFile(path='cambridge.jpg')
    keyboard = create_keyboard()
    await message.answer_photo(photo=photo, caption=text, reply_markup=keyboard)


@rg.message(States.start_menu)
async def check_menu_buttons(message:types.Message, state:FSMContext):
    info = info_retrieve()[0]
    if message.text in info[4].split(';'):
        chosen_button = message.text
        print(chosen_button)
    else:
        print(info[4].split(';'))
        print('eckjdbt ')


#async def check_menu_buttons(message:types.Message):
    #pass

async def fill_form(message:types.Message):
    pass

async def show_vacancy(message:types.Message):
    pass

async def choose_branch(message:types.Message):
    pass



async def main():
    await dp.start_polling(bot)

asyncio.run(main())
