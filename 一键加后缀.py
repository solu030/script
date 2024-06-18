import os #导入模块
filename = "D:\\xx"
list_path = os.listdir(filename)  #读取文件夹里面的名字
pass_dir = ['SteamLibrary','tools',"System Volume Information","$RECYCLE"] #需要跳过的文件夹
for index in list_path:  #list_path返回的是一个列表   通过for循环遍历提取元素
    txt = index.split('.',)  #split字符串分割的方法 , 分割之后是返回的列表 索引取第一个元素[0]
    if len(txt) != 2:
        continue
    name = txt[0]
    end = txt[1]
    path = filename + '\\' + index
    new_path = filename + '\\'  + name + '.' + "7z"
    if name in pass_dir or end != "mp3":
        continue
    # print(new_path)
    os.rename(path, new_path) #重新命名

print("done")
