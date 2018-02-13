'''
Can use this for opening file by taking the directory of search as input to open_app
'''
import os
def winsearch(string):
    found = 0
    for root, dirs, files in os.walk('C:\\'):
      #print("searching", root)
      if string in files:
        path = root + "\\" + string
        print(path)
        return(path)
        found = 1
        break

    if not found:
        for root, dirs, files in os.walk('A:\\'):
            #print("searching", root)
            if string in files:
                path = root + "\\" + string
                print(path)
                return (path)
                found = 1
                break

    if not found:
        for root, dirs, files in os.walk('B:\\'):
            #print("searching", root)
            if string in files:

                path = root +"\\" + string
                print(path)
                return (path)
                found = 1
                break
    if not found:
        for root, dirs, files in os.walk('D:\\'):
            #print("searching", root)
            if string in files:

                path = root +"\\" + string
                print(path)
                return (path)
                found = 1
                break
    if not found:
        print("File is not present")
        return ""