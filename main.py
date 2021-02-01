import shutil, os
from pathlib import Path
from sys import platform

folders = ['Executables', 'PDFs', 'Video', 'Other', 'ZIP', 'Images', 'Text', 'Audio', 'Torrents', 'Slides']
downloads_path = str(Path.home() / "Downloads")

# Program only runs on windows for now
def OScheck():
    if platform == "win32":
        nav_folder()

def nav_folder():
    for folder in folders:
        if os.path.isdir(downloads_path + './' + folder) == False:
            try:
                os.mkdir(downloads_path + './' + folder)
            except OSError:
                print("Creation of the folder %s failed" % folder)
            else:
                print("%s folder succesfully created" % folder)
    file_move()

def file_move():
    for filename in os.listdir(downloads_path):
        try:
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
            elif filename.lower().endswith(('.MP4', '.AVI', '.MOV', '.mp4')):
                shutil.move(downloads_path + './' + filename, downloads_path + './Video' + './' + filename )
            elif filename.lower().endswith(('.MP3', '.mp3')):
                shutil.move(downloads_path + './' + filename, downloads_path + './Audio' + './' + filename )
            elif filename.lower().endswith(('.torrent')):
                shutil.move(downloads_path + './' + filename, downloads_path + './Torrents' + './' + filename )
            elif filename.lower().endswith(('.pptx', '.ppt')):
                shutil.move(downloads_path + './' + filename, downloads_path + './Slides' + './' + filename )
        except FileNotFoundError:
            print("The system could not find the specified path for %s, please check again." % filename)

if __name__ == "__main__":
    OScheck()
