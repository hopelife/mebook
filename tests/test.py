# -*- coding: utf-8 -*-
import os
import codecs

# path내에 있는 ext 확장자 파일 목록 얻기
def listFiles(path="../literature/_source/selfmade/", ext=".txt"):
    return [file for file in os.listdir(path) if file.endswith(ext)]


# path내에 있는 ext 확장자 파일 합치기
def mergeFiles(path="../literature/_source/selfmade/", ext=".txt"):
    fm = open(path + "merged.txt", mode="wt", encoding="utf-8")
    content = ""
    #with codecs.open(path + "merged.txt", "r", encoding='utf-8', errors='ignore') as fm:
    for file in os.listdir(path):
        if file.endswith(ext):
            print(file)
            r = codecs.open(path + file, "r", encoding='utf-8', errors='ignore')
            content += "\n======\n" + file + "\n------\n" + r.read()
            r.close()

    fm.write(content)
    fm.close()


# path내에 있는 name 파일 기초적인 수정 작업
def amendFile(path="../literature/_source/selfmade/", name="merged.txt"):
    fn = path + name
    with codecs.open(path + "merged.txt", "r", encoding='utf-8', errors='ignore') as fm:
        r = open(fn, "r", encoding='utf-8')
        content = r.read()
        // to do
        r.close()


#-------------------------------
# main function
#-------------------------------
# 실행 mergyFiles("../literature/_source")
if __name__ == '__main__':
    #env = get_json(sys.argv[1])
    mergeFiles()
