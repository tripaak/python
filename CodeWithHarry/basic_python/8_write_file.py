f = open('akash.txt','r+',newline='\n')

print(f.read())

f.write("Line4\n")   #.write() to write files 

print(f.write("Akash"))  # retuns number of character written 

f.close()