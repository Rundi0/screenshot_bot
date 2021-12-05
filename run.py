from aiogram import executor
from aiogram.types import Message

from config import bot, dp, browserHandler, PATH_IMAGE

@dp.message_handler(commands=["help"])
async def handle_command_help(message: Message):
    await bot.send_message(
        message.from_user.id,
        text="Скиньте боту URL!",
    )

@dp.message_handler()
async def handle_command_help(message: Message):
    browserHandler.get(message.text)
    browserHandler.get_screenshot_as_file(PATH_IMAGE)
    await bot.send_document(chat_id=message.chat.id, document=open(PATH_IMAGE,"rb"))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
