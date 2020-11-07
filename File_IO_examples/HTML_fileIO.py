## Excerice Extract web links from html file .

with open('index.html', 'r') as sf:
    with open('output.txt','a') as df:
        # print(sf.readlines())
        for line in sf.readlines():
            if '<a href=' in line:
            #   print(line)
                pos =line.find('\"')
                pos1 = line.find('\"',pos + 1)
                link = line[pos+1:pos1]
                df.write(f"{link}\n")
