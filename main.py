

#function for checking identity
def check_our_files(path1, path2):
    str1 = getData(path1)
    str2 = getData(path2)

    
#get data from the wile
def getData(path):
    file = open(path,'r')
    result = []

    for str in file:
        str = str.replace("\n", "")
        result.append(str)
    file.close()
    return result
#write data in the file
def writeFile(path:str, data):
    result_file = open(path, "w")
    result_file.truncate()
    for el in data:
        result_file.write(el+"\n")
    result_file.close()
    
#start of the function
check_our_files("file1.txt", "file2.txt")