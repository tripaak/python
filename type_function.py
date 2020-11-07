# # import cx_oracle
# import cx_Oracle
# conn = cx_Oracle.connect('')
# cur = conn.cursor()
# cur.execute('select * from atlas.company')

# for row in cur:
#     print(row)






###################################################
number = [1,2,3,4, [4,5,6],[1,2]]


def check_lists(num):
    num_list = 0
    for i in num:
        is_list = type(i)
        if is_list == list : 
            num_list += 1
    return num_list


print(check_lists(number))