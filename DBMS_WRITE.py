import pyautogui
import time
import win32clipboard
from termcolor import colored
import mysql.connector

mydb = mysql.connector.connect(
        host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()

# print(pyautogui.position())
# 82, 1107
# 462, 1374

def location():
    print(pyautogui.position())

def WriteCode(Code):
    pyautogui.click(1471, 864)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.keyDown("delete")
    pyautogui.typewrite(Code)

def GetData():
    pyautogui.click(56, 816)
    pyautogui.keyDown('shift')
    pyautogui.click(297, 1023)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.hotkey("ctrl","c")
    time.sleep(0.1)
    #print("Getting Question Name..")
    win32clipboard.OpenClipboard()
    Question = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    #print(Question)
    Sstart = Question.find("QUESTION NAME: ")
    Estart = Question.find("TABLE DESCRIPTION")
    # print(Sstart)
    # print(Sstart)
    # #print()
    Sess = Question[0:Sstart-1]
    Sess = Sess[13:]
    Quest = Question[Sstart:Estart-1]
    Quest = Quest[15:]

    Sess = str(Sess).replace('\r', '')
    Sess = str(Sess).replace('\n', '')
    Quest = str(Quest).replace('\r', '')
    Quest = str(Quest).replace('\n', '')
    sql = "SELECT CODE from data WHERE SESSION = '" + Sess + "' AND QUESTION = '" + Quest + "'"
    # sql = "SELECT CODE from data WHERE SESSION = 'Joins and Unions-1'"
    mycursor.execute(sql)
    # try:
    try:

        result = mycursor.fetchall()[0]

    except:

        result = mycursor.fetchone()

    if result != None:
        Code = result[0]
        print("Coding...")
        WriteCode(result[0])
    else:
        Code = "No Code"
        err = colored('Error : ', 'red')
        text = colored('Code not Found. Need to Code Manually..', 'green')
        print(err + text)
    # except:
    #     Code = "Error Code"

    print()
    print(colored("QUESTION", "green"))
    print(Sess)
    print(Quest)
    print(colored("Answer", "green"))
    print(Code)
    print()
    # sql = "INSERT INTO data (SESSION, QUESTION, CODE) VALUES (%s, %s, %s)"
    # data = []
    # data.append(Sess)
    # data.append(Quest)
    # data.append(Answer)
    # data = tuple(data)
    # mycursor.execute(sql, data)
    # # print(mycursor)
    # mydb.commit()
    time.sleep(1)


def Loadpage(val):
    pyautogui.click(1742, 126)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl","a")
    time.sleep(0.5)
    pyautogui.keyDown("delete")
    time.sleep(0.5)
    pyautogui.keyUp("delete")
    URL = "https://care.srmist.edu.in/mysqlelabsh/login/student/code/dbms/dbms.code.php?id=1&value="+str(val)
    pyautogui.typewrite(URL)
    print(URL)
    time.sleep(0.5)
    pyautogui.keyDown('enter')

for i in range(0, 100):
    print(colored("Question "+str(i+1), "red"))
    Loadpage(i)
    time.sleep(0.5)
    GetData()
    time.sleep(1)
    pyautogui.click(2716, 1812)
    time.sleep(5)
# location()
# GetData()