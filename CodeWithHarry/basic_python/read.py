from csv import DictReader
import os


cred = {}

os.chdir(r"C:\Users\akash.tripathi\Desktop\python1.0\CodeWithHarry\basic_python")


csv_file = open("kapp_users.csv",'r')
csv_reader = DictReader(csv_file)
for cred_list in csv_reader:
    cred = {
        "autocomplete": "false",
        "isVirtualKeyboardHidden":"true",
        }
    # print(cred_list.get('name'))
    cred.update({
        "j_username":str(cred_list.get("company") + '@' + cred_list.get('name')), #"PRODUCTMAT@LOAD003"
        "k_password":str(cred_list.get("password")) #pYYGwqeTDc03
    })

    print(cred)