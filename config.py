import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import FirefoxOptions
PATH_IMAGE = "./image.png"

logging.basicConfig(level=logging.DEBUG)

API_TOKEN = "5030402277:AAHDm0p3e-vqzzWn7ajVqs4LqtPrJMcj9rg"

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

opts = FirefoxOptions()
opts.add_argument("--headless")
browserHandler = webdriver.Firefox(options=opts, executable_path="./geckodriver")
browserHandler.set_window_size(1920, 1080, browserHandler.window_handles[0])


