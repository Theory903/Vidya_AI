from Model.UI.Discord_Api import client,discord_tokens
from Model.AI.File_Org import organize_files_by_extension

if __name__=="__main__":
    client.run(discord_tokens)
    # Specify the source directory where the files are located
    source_directory = 'AIBOT/docs'
    # Call the function to organize files by extension
    organize_files_by_extension(source_directory)