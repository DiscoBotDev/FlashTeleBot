from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import gspread
from oauth2client.service_account import ServiceAccountCredentials

bot = Bot(token='Insert')
dp = Dispatcher(bot)

scope = ['Insert']
creds = ServiceAccountCredentials.from_json_keyfile_name('Insert', scope)
client = gspread.authorize(creds)

sheet = client.open("Insert").sheet1

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        await message.reply("Hi!\nI'm Flash Giveaway Bot.!\n My job is to give away Flash tokens. \
        	\n In order to get Flash tokens type the following command: /giveaway (FlashAddress). \
        	\n Please Note: replace (FlashAddress) with your actual Flash wallet address. Thanks!")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
		print(str(message))
		await message.reply("Here are the commands I offer /help, /start, /giveaway.")

@dp.message_handler(commands=['giveaway'])
async def send_welcome(message: types.Message):
		Username = message['chat']['username']
		address = message['text'].split(" ");
		# print(Username)
		# print(address)
		row = [Username, address[1]]
		records = sheet.get_all_records()
		index = len(records)+2
		if checkRecords(Username) == True:
			await message.reply("Username already in sheet.")
		else:
			sheet.insert_row(row,index)

def checkRecords(Username):
	records = sheet.get_all_records()
	for record in records:
		if str(record['Username:']) == str(Username):
			return True
		else:
			return False


if __name__ == '__main__':
        executor.start_polling(dp)