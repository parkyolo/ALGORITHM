import os
path = r"C:\Users\jiyou\Documents\ALGORITHM\Baekjoon\SILVER3"
filenames = os.listdir(path)
for file1 in filenames:
    os.rename(path+"\\"+file1, path+"\\"+"S3_"+file1)
