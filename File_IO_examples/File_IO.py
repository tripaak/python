# ## Execrcise 
# Read name and salary from salary.txt file 
# create new file as summery.txt
# write for e.g. Akash has salary of xyz.


with open('salary.txt','r') as sf:
    with open('summery.txt', 'a') as df:
        #print(type(sf.readlines()))       readlines saves each line as list 
        for line in sf.readlines():
            # print(line)
            name,salary = line.split(',')
            df.write(f"{name} has salary of {salary}")