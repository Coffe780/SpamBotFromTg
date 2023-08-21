try:
	import os
	from time import sleep
	from pyrogram import Client, filters
	from art import *
	os.system("clear")
	print("Все модули установлены!")
	tprint("By Artom")	
except:
	print("Модули не установлены, начинаю скачивание...")
	os.system("pip install pyrogram tgcrypto art")
	os.system("clear")
	import os
	from time import sleep
	from pyrogram import Client, filters
	from art import tprint
	tprint("By Artom")
	

api_hash="ArtomMegaKrutoi"
api_id=123456
	

app=Client("my_account", api_id=api_id, api_hash=api_hash)
@app.on_message(filters.me)
async def msg(client, msg):
	
	if msg.text.split()[0].lower() == "-spam":
		
		text=msg.text.split(maxsplit=2)[2]
		
		count=int(msg.text.split(maxsplit=2)[1])
		
		await client.delete_messages(msg.chat.id, msg.id)
		for i in range(count):
			try:
				await msg.reply(text)
				sleep(0.005)
			except:
				sleep(0.04)
				
if __name__=="__main__":	
	app.run()
		


