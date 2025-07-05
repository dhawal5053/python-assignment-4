file_name = 'sample.txt'
try:
    file = open(file_name,'r')
    file_read = file.readlines()
    print('Reading file content:')
    num = 1
    for i in file_read:
        print('Line '+str(num)+':',i)
        num+=1
    file.close()
except:
    print('Error: The file \''+file_name+'\' was not found.')