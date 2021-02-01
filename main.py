import shutil, os
from pathlib import Path
from sys import platform

""" DISCLAIMER: I am not responsible for any files aciddentally lost/deleted. Only run this script on files you have a back up for or can redownload! """

folders = ['Executables', 'PDFs', 'Video', 'Other', 'ZIP', 'Images', 'Text', 'Audio', 'Torrents', 'Slides']
downloads_path = str(Path.home() / "Downloads")

# Program only runs on windows for now
def OScheck():
    if platform == "win32":
        nav_folder()
    else:
        print("Please run this script on a device running Windows.")

def nav_folder():
    for folder in folders:
        if os.path.isdir(downloads_path + './' + folder) == False:
            try:
                os.mkdir(downloads_path + './' + folder)
            except OSError:
                print("Creation of the folder %s failed" % folder)
            else:
                print("%s folder succesfully created" % folder)          
    file_move_category()

def file_move_category():
    for filename in os.listdir(downloads_path):
        if filename.lower().endswith(('.pdf')):
            shutil.move(downloads_path + './' + filename, downloads_path + './PDFs' + './' + filename )
        elif filename.lower().endswith(('.exe', '.msi')):
            shutil.move(downloads_path + './' + filename, downloads_path + './Executables' + './' + filename )
        elif filename.lower().endswith(('.txt', '.doc', '.docx', '.xls', '.xlsx', '.ods')):
            shutil.move(downloads_path + './' + filename, downloads_path + './Text' + './' + filename )
        elif filename.lower().endswith(('.zip', '.rar', '.7z')):
            shutil.move(downloads_path + './' + filename, downloads_path + './ZIP' + './' + filename )
        elif filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            shutil.move(downloads_path + './' + filename, downloads_path + './Images' + './' + filename )
        elif filename.lower().endswith(('.AVI', '.MOV', '.mp4')):
            shutil.move(downloads_path + './' + filename, downloads_path + './Video' + './' + filename )
        elif filename.lower().endswith(('.mp3')):
            shutil.move(downloads_path + './' + filename, downloads_path + './Audio' + './' + filename )
        elif filename.lower().endswith(('.torrent')):
            shutil.move(downloads_path + './' + filename, downloads_path + './Torrents' + './' + filename )
        elif filename.lower().endswith(('.pptx', '.ppt')):
            shutil.move(downloads_path + './' + filename, downloads_path + './Slides' + './' + filename )
        else:
            target_dir = os.path.join(downloads_path, '.\Other')
            file_move_remaining(target_dir)

# Move remaining files to the 'Other' folder
def file_move_remaining(target_dir):
    for filename in os.listdir(downloads_path):
        if os.path.isfile(os.path.join(downloads_path, filename)) == True:
            shutil.move(os.path.join(downloads_path, filename), os.path.join(target_dir, filename))

if __name__ == "__main__":
    OScheck()
