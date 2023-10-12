#IMPORTS
from dotenv import load_dotenv
import discord
import os
import datetime
from Model.AI.Bot import AI 

# LOAD (.env) FILE
load_dotenv()

# FETCH DISCORD API KEY
discord_tokens = os.getenv('DISCORD_TOKEN')

# Define the folder to save chat history files
chat_history_folder = 'ChatHistory'

# Create the folder if it doesn't exist
if not os.path.exists(chat_history_folder):
    os.mkdir(chat_history_folder)

# MYCLIENT CLASS
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user.name} Logged on as {self.user}!')
    async def on_message(self, message):
        
    # TRY THIS 
        try:
            chat = ""
            chat += f"{message.author}: {message.content}\n"
            prompt = f"{chat}\nVidyaAI: "
            print(f'Message from {message.author}: {message.content}')
            if self.user!= message.author:
                if message.content == message.content:
                    response = AI(prompt)
                    channel = message.channel
                    messageToSend = response
                    await channel.send(messageToSend) 
                    # Create a separate .txt file for each chat history with date and time
                    current_date = datetime.date.today()
                    chat_file_name = f'{message.author}_{current_date}_chat_history.txt'
                    chat_file_path = os.path.join(chat_history_folder, chat_file_name)
                    with open(chat_file_path, 'a') as chat_file:
                        chat_file.write(prompt)  
                        chat_file.write(messageToSend+'\n') 
                elif message.attachments:
                    download_folder = "AIBOT/docs"
                    for attachment in message.attachments:
                        # Construct the download path
                        download_path = os.path.join(download_folder, attachment.filename)
                        # Download the file
                        await attachment.save(download_path)
                        print(f"Downloaded: {attachment.filename}")        
        # IF ERROR THROUGH EXCEPTION    
        except Exception as e:
            print(e)
            chat = ""
# DISCORD SERVER INTENT
intents=discord.Intents.default()
intents.message_content= True
client=MyClient(intents=intents)