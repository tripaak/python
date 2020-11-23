# write a program to plot '|' charcters garph on consoile screen for given list of whole numbers as heights .

# for example plot graphs for [8,2,5,4,1,3]


# def graph_plotter(sample_list):
#     flag = False
#     for sample in sample_list:
#         if flag == True:
#            print('----------',end='')
#         flag = True
#         for i in range(1,sample+1):
#             print('|')
    
def graph_plotter(nums): #1 method 
    m = max(nums)
    # a= ['|']
    # b = ['']
    # print(a+b)
    lines = [['|']*n + ['']*(m-n) for n in nums] # producing rows of '|'
    # print(lines)
    print('\n')
    # print(tuple(zip(*lines)))
    # print(tuple(zip(*lines))[::-1])
    # print('\t'+'\t'.join(('|', ''))) 
    for line in tuple(zip(*lines))[::-1]: # transpose of lines 
        print('\t'+'\t'.join(line)) 
    print('\t'+'-'*(len(nums)*8-7)) #printng dash line of bases 
    print('\t'+'\t'.join(map(str,nums))) # printing nums below dash line 

def plot_bars(a): #2 method 
    rows=[("|"*i).rjust(max(a),' ') for i in a]
    [print(*i,sep="\t") for i in zip(*rows)]
    print("-"*(8*len(a)-7))
    print(*a,sep="\t")    





if __name__ == "__main__":
    data_sample = [4,2]
    graph_plotter(data_sample)