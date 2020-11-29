import requests
import re
from csv import DictReader
import os





# LOAD000- LOAD003 Done

# {"csrf":{"token":"NCD9-68GQ-NNFG-YSA3","tokenName":"KA5HLVOX2B7N6H5Z","loginPageToken":"1606229280814"}

## Step 0 read data from csv file 



os.chdir(r"C:\Users\akash.tripathi\Desktop\python1.0\CodeWithHarry\basic_python")


csv_file = open("kapp_users.csv",'r')
csv_reader = DictReader(csv_file)
# session = requests.session()
for cred_list in csv_reader:
    session = requests.session()
    cred = {
        "autocomplete": "false",
        "isVirtualKeyboardHidden":"true",
        }
    # print(cred_list.get('name'))
    cred.update({
        "j_username":str(cred_list.get("company") + '@' + cred_list.get('name')), #"PRODUCTMAT@LOAD003"
        "k_password":str(cred_list.get("password")) #pYYGwqeTDc03
    })

    # print(cred)

    print(cred)



    # # Step 1 : Home Page 

    homepage_url = "https://diamond-preprod.treasury-factory.com/user/login"



    req = session.post(homepage_url)#,data=cred)

    x = re.findall(r"{\"token\":\"(.+?)\",\"tokenName\":\"(.+?)\",\"loginPageToken\":\"(.+?)\"}", str(req.content))

    print(f"values of x is :")


    cred.update({
        str(str(x[0][1])) : str(x[0][0]),
        "loginPageToken" : str(x[0][2])

    })



    # # Step 2 : Login to Kyriba 

    login_url = "https://diamond-preprod.treasury-factory.com/j_security_check"

    # print(cred)

    login = session.post(login_url,data=cred)

    ## Post Step 2 urls

    session.get("https://diamond-preprod.treasury-factory.com/")
    session.get("https://diamond-preprod.treasury-factory.com/to_top.jsp")
    session.get("https://diamond-preprod.treasury-factory.com/kiwi")



    #Step 3 : Load /Kiwi session

    kiwi = session.get("https://diamond-preprod.treasury-factory.com/kiwi")

    # print(kiwi.content)

    regex_kiwi = r"{\"token\":\"(.+?)\",\"tokenName\":\"(.+?)\",\"loginPageToken\":\"(.+?)\"}"

    y = re.findall(regex_kiwi,str(kiwi.content))

    # print(kiwi.content)

    # print(y)




    payload = {
                "agreeCheckbox":"true",
                "action":"accept",
                "loginPageToken":str(y[0][2]),
                str(str(x[0][1])):str(y[0][0])

    }

    accept_notice = session.post("https://diamond-preprod.treasury-factory.com/notice_acceptance",data= payload)

    # print(accept_notice.content)
    
    print("Process is finished for user: ",cred.get("j_username"))

