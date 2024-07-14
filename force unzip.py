import itertools
import sys
import os
import zipfile
import py7zr
import rarfile


class UnCompress:
    def __init__(self, file_path, output_path, password=None):
        self.file_path = file_path  # 输入文件路径
        self.output_path = output_path  # 输出文件路径
        self.password = password  # 压缩密码

    # zip解压缩
    # 这里修改了zipfile源码，默认改为了utf-8和gbk解码，修复了中文压缩包乱码问题
    def unzip_file(self):
        with zipfile.ZipFile(file=self.file_path, mode='r') as fp:
            fp.extractall(self.output_path, pwd=self.password.encode('ascii'))

    # 7z解压缩
    def un7z_file(self):
        with py7zr.SevenZipFile(self.file_path, 'r', password=self.password) as fp:
            fp.extractall(path=self.output_path)

    # RAR解压缩
    def unrar_file(self):
        with rarfile.RarFile(self.file_path, 'r') as fp:
            fp.extractall(self.output_path, pwd=self.password)

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


if __name__ == '__main__':
    max_len = 10  #最长位数
    file_dir = "D:\\"
    out_path = "D:\\"
    file_name = 'demon city.zip'  #暴力破解时需要自己输入文件名
    prob_pwd = ["哈哈", "呃呃", "5iD"]

    # itertools.product返回生成对象
    p_string = ''
    pwd_len = 1
    for i in range(97, 123):
        p_string = p_string + chr(i)
    for i in range(65, 91):
        p_string = p_string + chr(i)
    for i in range(48, 58):
        p_string = p_string + chr(i)

    w_input = file_dir + '\\' + file_name
    a = UnCompress(w_input, out_path)

    #先进密码字典里破解
    for i in prob_pwd:
        try:
            print("当前密码:" + i)
            a.password = i
            a.run()
            print("破解成功，密码为:" + a.password)
            sys.exit()
        except Exception as e:
            continue

    while pwd_len <= max_len:
        pwd_list = ("".join(x) for x in itertools.product(p_string, repeat=pwd_len))
        for i in pwd_list:
            try:
                print("当前密码:" + i)
                a.password = i
                a.run()
                print("破解成功，密码为:" + a.password)
                sys.exit()
            except Exception as e:
                continue
        pwd_len += 1
