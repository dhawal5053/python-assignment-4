file_name = 'output.txt'
input1 = input('Enter text to write to the file: ')
file1=open(file_name,'w')
write = file1.write(input1)
print('Data successfully written to'+file_name+'\n')
file1.close()

input2 = input('Enter additional text to append: ')
file1=open(file_name,'a')
append = file1.write('\n'+input2)
print('Data successfully appended.\n')
file1.close()

file1=open(file_name,'r')
read_file = file1.read()
print('Final content of '+file_name+':')
print(read_file)
file1.close()

