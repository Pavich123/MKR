#check for the same
def checkForSame(str1, str2):
    same = []
    for el in str1:
        if el in str2:
            same.append(el)
    return same

#check for the difference
def checkForDiff(str1, str2):
    diff = []
    for el in str1:
        if el not in str2:
            diff.append(el)
    return diff

#function for checking identity
def check_our_files(path1, path2):
    str1 = getData(path1)
    str2 = getData(path2)

    res1 = checkForSame(str1, str2)
    res2 = checkForDiff(str1, str2)

    for el in checkForDiff(str2, str1):
        res2.append(el)

    writeFile("result_with_difference.txt", res2)
    writeFile("same_result.txt", res1)
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