import os
import shutil

from time import sleep


class Organize:
    def __init__(self):
        self.mypath = ""
        self.file_type_variation_list = []
        self.filetype_folder_dict = {}

    def run(self, path):
        self.mypath = path
        files = self.get_files()
        self.create_folders(files)
        self.move_files(files)

    def get_files(self):
         return [f for f in os.listdir(self.mypath) if os.path.isfile(os.path.join(self.mypath, f))]

    def create_folders(self, files):
        for file in files:
            filetype = file.split('.')[-1]
            if filetype not in self.file_type_variation_list: 
                self.file_type_variation_list.append(filetype) 
                new_folder_name = os.path.join(self.mypath, filetype + '_folder')
                self.filetype_folder_dict[str(filetype)] = str(new_folder_name)
                if os.path.isdir(new_folder_name):
                    continue 
                else:
                    os.mkdir(new_folder_name)

    def move_files(self, files):
        for file in files:
            src_path = os.path.join(self.mypath, file)
            filetype = file.split('.')[-1]
            filename = " ".join(file.split('.')[:-1])
            if filetype in self.filetype_folder_dict.keys(): 
                dest_path = self.filetype_folder_dict[str(filetype)]

                if os.path.isfile(f"{dest_path}\\{file}"):
                    for i in range(2, 1000):
                        if not os.path.isfile(f"{dest_path}\\{filename} ({str(i)}).{filetype}"):
                            os.rename(src_path, f"{self.mypath}\\{filename} ({str(i)}).{filetype}")
                            src_path = os.path.join(self.mypath, f"{filename} ({str(i)}).{filetype}")
                            break

                shutil.move(src_path, dest_path)


if __name__ == "__main__":
    organize = Organize()
    download_loc = os.path.join(os.environ["USERPROFILE"], "Downloads")

    while True:
        if os.path.isdir(download_loc):
            organize.run(download_loc)
        sleep(30)
