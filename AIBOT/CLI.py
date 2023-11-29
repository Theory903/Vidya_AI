from Model.AI.Bot import AI 
import os
import datetime
# Define the folder to save chat history files
chat_history_folder = 'ChatHistory'

# Create the folder if it doesn't exist
if not os.path.exists(chat_history_folder):
    os.mkdir(chat_history_folder)

while True:
    
    prompt=input("USER: ")
    current_date = datetime.date.today()
    chat_file_name = f'{current_date}_chat_history.txt'
    chat_file_path = os.path.join(chat_history_folder, chat_file_name)
    if prompt=="quit":
        break
    else:
        AI(prompt)
        print()