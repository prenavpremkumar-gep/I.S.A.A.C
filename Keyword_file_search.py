#This code is useful when you really don't remember the exact name of file to be searched
import glob,os
found = 0
file_name = input('Enter a keyword to search file: ')
matches = []
for dirname, dirnames, filenames in os.walk('C://'):
     for i in glob.glob(dirname+'/*'+file_name+'*'):
         matches.append(i)
         found =1
for dirname, dirnames, filenames in os.walk('F://'):
     for i in glob.glob(dirname+'/*'+file_name+'*'):
         matches.append(i)
         found =1

if found ==1:
    for idx,value in enumerate(matches):
        print(idx,value+'\n')
    ind = int(input('Enter a file index to open: '))
    for idx, value in enumerate(matches):
        if idx == ind:
            value = os.path.abspath(value)
            print (value)
            os.startfile(value)

if found==0:
    print('File not found')
