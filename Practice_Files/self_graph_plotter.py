def graph_plot(nums):
    m = max(nums)
    lines = []
    new_lines = []
    for n in nums:
        lines.append(['|']*n + ['']*(m-n))
    # print(f"Printing lines list: {lines}") 
    for i in range(0,len(lines)):
        new_lines.append(lines[i][::-1])
    # print(new_lines)
    for item in tuple(zip(*new_lines)):
        print('\t'+'\t'.join(item))
    print('\t'+'-'*9*(len(nums)-1)) 
    print('\t'+'\t'.join(map(str,nums))) 






graph_plot([4,2,3,4,8,10,5,9,5])