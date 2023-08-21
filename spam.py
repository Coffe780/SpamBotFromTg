import os
from time import sleep
try:
	from pyrogram import Client, filters
	print("Все модули установлены")
except:
	print("Модуль не найден, начинаю установку...")
	os.system("pip install pyrogram tgcrypto")
	os.system("clear")
	print("Модули установлены")
	from pyrogram import Client, filters
	
api_id=int(open("token.txt").read().split(sep="\n")[1].replace("api_id=",""))

api_hash=open("token.txt").read().split(sep="\n")[0].replace("api_hash=","")

app=Client("my_account", api_id=api_id, api_hash=api_hash)
@app.on_message(filters.me)
async def msg(client, msg):
	
	if msg.text.split()[0].lower() == "-spam":
		
		text=msg.text.split(maxsplit=2)[2]
		
		float(count=msg.text.split(maxsplit=2)[1])
		
		client.delete_message(msg.chat.id, msg.id)
		for i in range(count):
			try:
				msg.reply(text)
				sleep(0.005)
			except:
				sleep(0.04)
if __name__=="__main__":	
	app.run()
		


