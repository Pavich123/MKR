def check_our_files(path1, path2):
    str1 = getData(path1)
    str2 = getData(path2)
    print(str1,str2)

def getData(path):
    file = open(path,'r')
    result = []

    for str in file:
        result.append(str)
    file.close()
    return result


check_our_files("file1.txt", "file2.txt")