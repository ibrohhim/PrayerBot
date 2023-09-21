from config import TOKEN
from aiogram import Dispatcher,Bot
from aiogram.types import Message,CallbackQuery
from prayrequests import Prayrequests
from praytime import Praytime
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from asyncio import run
from aiogram import F
from aiogram.filters.callback_data import CallbackData 


class MainBot:
    def __init__(self,token = TOKEN)->None:
        self.__dp = Dispatcher()
        self.__bt = Bot(token = token)
        ls_btn = ["Toshkent","Andijon","Samarqand","Buxoro","Fargona","Xorazm","Namangan","Jizzax"]
        box =  InlineKeyboardBuilder()
        for reg in ls_btn:
            box.add(InlineKeyboardButton(text=reg,callback_data="reg:"+reg))
        box.adjust(4,4)
        self.bx = box.as_markup()

    async def start_message(self,msg:Message):

        await msg.answer(text = "Assalomu aleykum viloyatigizni tanlang!",reply_markup = self.bx)

    async def region_callback(self, clb:CallbackQuery):
        data = clb.data.split(":")
        vil = data[1]
        pr = Prayrequests(vil)
        pr.request()
        print('He')
        pt = Praytime(pr.Content)
        pt.scrapping()
        print("salom")
        await clb.message.answer(f"Ayni vaqitdagi {vil} dagi namoz vaxtlari:",reply_markup=pt.get_keyboards())

        await clb.answer(text = "ANSWER")

    def register(self):
        self.__dp.message.register(self.start_message, Command("start"))
        self.__dp.callback_query.register(self.region_callback)

    async def start(self):
        try:
            self.register()
            await self.__dp.start_polling(self.__bt)
        except:
            await self.__bt.session.close()

if __name__ == "__main__":
    mn = MainBot()
    run(mn.start())
