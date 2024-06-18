import os #导入模块
filename = "D:\\"
list_path = os.listdir(filename)  #读取文件夹里面的名字
for index in list_path:  #list_path返回的是一个列表   通过for循环遍历提取元素
    ls = index.split('.')
    if len(ls)<2:
        continue
    end = ls[-1]
    txt = index.split('A')  #split字符串分割的方法 , 分割之后是返回的列表 索引取第一个元素[0]
    end = txt[-1]
    path = filename + '\\' + index
    new_path = filename + '\\'  + 'A' + end
    if  end not in ["mp3","flac","m4a"]:
        continue
    # os.rename(path, new_path) #重新命名
    print(new_path)
print("done")