import os
import zipfile
import py7zr
import rarfile
 
 
class UnCompress:
    def __init__(self, file_path, output_path, password=None):
        self.file_path = file_path                  # 输入文件路径
        self.output_path = output_path              # 输出文件路径
        self.password = password                    # 压缩密码
 
    # zip解压缩
    def unzip_file(self):
        try:
            with zipfile.ZipFile(file=self.file_path, mode='r') as fp:
                fp.extractall(self.output_path, pwd=self.password.encode('ascii'))
            return True
        except:
            return False
 
    # 7z解压缩
    def un7z_file(self):
        try:
            with py7zr.SevenZipFile(self.file_path, 'r', password=self.password) as fp:
                fp.extractall(path=self.output_path)
            return True
        except:
            return False
 
    # RAR解压缩
    def unrar_file(self):
        try:
            with rarfile.RarFile(self.file_path, 'r') as fp:
                fp.extractall(self.output_path, pwd=self.password)
            return True
        except:
            return False
 
 
    def run(self):
        file_state = False
        if not os.path.exists(self.file_path):
            return file_state
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
 
        # zip解压缩
        if zipfile.is_zipfile(self.file_path):
            file_state = self.unzip_file()
 
        # 7z解压缩
        if py7zr.is_7zfile(self.file_path):
            file_state = self.un7z_file()
 
        # RAR解压缩
        if rarfile.is_rarfile(self.file_path):
            file_state = self.unrar_file()
 
        return file_state

file_dir = "D:\\xx"
file_list = os.listdir(file_dir)
out_path = "D:\\xx"
password = "xxx"

for file_name in file_list:  # 循环读文件
    full_name = file_name.split(".")
    end_name = full_name[1]
    if len(full_name) != 2 or end_name not in ["7z","zip","rar"]:
        continue
    fore_name = full_name[0]
    w_input=file_dir + '\\'+ fore_name + '.' + end_name
    
    a=UnCompress(w_input,out_path,password)
    a.run()
    print("unzipping...")

print("done!")