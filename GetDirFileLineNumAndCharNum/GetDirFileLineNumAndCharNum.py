# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time
import os
#获得某个目录下的某格式文件的行数和字符数

#获取目录下的文件列表
def get_file_list(path):
    fileList=[]
    print(list(os.walk(path)))
    #得到指定路径下的根目录路径，根目录下的文件夹，根目录下的文件
    for root,dir,files in list(os.walk(path)):
        for i in files:
            if i.endswith('.md'):
                fileList.append(root+"\\"+i)
    print(fileList)
    return fileList

#统计文件中的行数和字符数
def oper_file(filePath):
    filePath=filePath
    with open(filePath,'r',encoding='utf-8') as file:
        content=file.readlines()
    file.close()
    lines=len(content)
    charNUm=0
    for i in content:
        charNUm+=len(i.strip('\n'))
    return lines,charNUm,filePath

#将结果写入文件中
def save_result(list1,savePath):
    fileLines=0
    charNum=0
    with open(savePath,'a',encoding='utf-8') as file:
        for i in list1:
            file.write("{0} 行数：{1} 字符数{2}\n".format(i[2],i[0],i[1]))
            fileLines+=i[0]
            charNum+=i[1]
    file.close()
    print(fileLines,charNum)


if __name__ == '__main__':
    #创建多进程并行处理目标目录中的目标格式文件的函数和字符数
    startTime=time.time()
    filePath="E:\\msysgit\\markdownPadNotes"
    fileList=get_file_list(filePath)
    pool=Pool(5)
    resultList=pool.map(oper_file,fileList)
    pool.close()
    pool.join()

    savePath="result.txt"
    print(resultList)
    save_result(resultList,savePath)
    endTime=time.time()
    print("Used time is {0}".format(startTime-endTime))


