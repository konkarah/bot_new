import telegram.ext
import mysql.connector
import requests
import jwt
import json
from jwt.exceptions import ExpiredSignatureError


TOKEN = '5448315119:AAGL4EwgtAH74p2znpj8_nIbLUhbgBjLgXk'

def start(update, context):
    update.message.reply_text("Hello, welcome to CCTPMIS")

def start(update, context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome Message
    /help -> This message
    /content -> information about CCTPMIS
    /contact -> informaion about Available Channels
    """)


def content(update, context):
    gettgid(update,context)
    verifyuser(userid)
    if status == True:
        update.message.reply_text("We offer several products")
    else:
        update.message.reply_text("You are not a verified user")

def contact(update, context):
    gettgid(update,context)
    verifyuser(userid)
    if status == True:
        update.message.reply_text("You can contact us via our official communication channels")
    else:
        update.message.reply_text("You are not a verified user")


def handle_message(update, context):
    gettgid(update,context)
    verifyuser(userid)
    if status == True:
        update.message.reply_text(f"You said {update.message.text}")
    else:
        update.message.reply_text("You are not a verified user")

#function to authenticate the default-user
def authentication():
    url = 'https://www.inuajamii.go.ke:1002/Token'
    myobj = {"grant_type": "password",
            "email": "itsthindi@gmail.com",
            "password": "@Amthindi2022"}

    x = requests.post(url, json = myobj)

    #return the access token
    print(x.text)

#function to get back id information 
def query(update, context):
    header = authentication()
    url = 'url'

    response = requests.get(url, headers = header)

    print(response.json)

    #loop through the json object and send back
    #info back to telegram

    update.message.reply_text()

def ctovc(pgno):
    mydb = mysql.connector.connect(
    host="192.168.64.2",
    user="deh",
    password="1234",
    database="CCTP"
    )

    mycursor = mydb.cursor()

    sql = "SELECT BankName,BranchName,AccountName,Amount FROM table_name WHERE ProgrammeNO = %s OR PrimaryRecipientNationalIDNO = %s"
    pgno = (pgno, )

    mycursor.execute(sql, pgno)

    myresult = mycursor.fetchall()

    for x in myresult:
        bankname = x[0]
        BranchName = x[1]
        AccountName = x[2]
        Amount = x[3]
        return f"BankName is: {bankname}\nBranch Name is: {BranchName} \nAccount Name is: {AccountName}\nPaid in last cycle: {Amount}"
    else:
        EXCEPTIONS(pgno) 


#Query the ctovc programme
def query_ctovc(update, context):
    gettgid(update,context)
    verifyuser(userid)
    if status == True:
        pgno = context.args[0]
        update.message.reply_text(ctovc(pgno))
    else:
        update.message.reply_text("You are not a verified user")
    

#pwsd function
def PWSD(pgno):
    mydb = mysql.connector.connect(
    host="192.168.64.2",
    user="deh",
    password="1234",
    database="CCTP"
    )

    mycursor = mydb.cursor()

    sql = "SELECT BankName,BranchName,AccountName,Amount FROM PWSD WHERE ProgrammeNO = %s"
    pgno = (pgno, )

    mycursor.execute(sql, pgno)

    myresult = mycursor.fetchall()

    for x in myresult:
        bankname = x[0]
        BranchName = x[1]
        AccountName = x[2]
        Amount = x[3]
        return f"BankName is: {bankname}\nBranch Name is: {BranchName} \nAccount Name is: {AccountName}\nPaid in last cycle: {Amount}"
    else:
        #return ("Not in payroll")
        EXCEPTIONS(pgno)


#Query the pwsd programme
def query_pwsd(update, context):
    gettgid(update,context)
    verifyuser(userid)
    if status == True:
        pgno = context.args[0]
        update.message.reply_text(PWSD(pgno))
    else:
        update.message.reply_text("You are not a verified user")

#Query the opct programme
def query_opct(update, context):
    gettgid(update,context)
    verifyuser(userid)
    if status == True:
        pgno = context.args[0]
        update.message.reply_text(opct(pgno))
    else:
        update.message.reply_text("You are not a verified user")

#opct function
def opct(pgno):
    mydb = mysql.connector.connect(
    host="192.168.64.2",
    user="deh",
    password="1234",
    database="CCTP"
    )

    mycursor = mydb.cursor()

    sql = "SELECT BankName,BranchName,AccountName,Amount FROM OPCT WHERE ProgrammeNO = %s"
    pgno = (pgno, )

    mycursor.execute(sql, pgno)

    myresult = mycursor.fetchall()

    for x in myresult:
        bankname = x[0]
        BranchName = x[1]
        AccountName = x[2]
        Amount = x[3]
        return f"BankName is: {bankname}\nBranch Name is: {BranchName} \nAccount Name is: {AccountName}\nPaid in last cycle: {Amount}"
    else:
        EXCEPTIONS(pgno)

#exceptions function
def EXCEPTIONS(pgno):
    mydb = mysql.connector.connect(
    host="192.168.64.2",
    user="deh",
    password="1234",
    database="CCTP"
    )

    mycursor = mydb.cursor()
    ReasonForException = ""

    #Without Payment Card
    WithoutPaymentCard = "SELECT * FROM WithoutPaymentCard WHERE ProgrammeNo =  %s"  
    WPCpgno = (pgno, )
    mycursor.execute(WithoutPaymentCard, WPCpgno)
    myresult1 = mycursor.fetchall()


    if len(myresult1) >= 1:
        ReasonForException +=  "Without Payment Card \n"
        

   
    #without Bank Account
    WithoutBankAccount = "SELECT * FROM WithoutBankAccount WHERE ProgrammeNo =  %s" 
    WBApgno = (pgno, )
    mycursor.execute(WithoutBankAccount, WBApgno)
    myresult2 = mycursor.fetchall()

    if len(myresult2) >= 1:
        ReasonForException +=  "Without Bank Account \n"
        

    #primary recipient IPRS mismatch
    PRIM = "SELECT * FROM PrimaryRecipientIPRSMismatch WHERE ProgrammeNo =  %s" 
    PRIMpgno = (pgno, )
    mycursor.execute(PRIM, PRIMpgno)
    myresult3 = mycursor.fetchall()

    if len(myresult3) >=1:
        ReasonForException +=  "Primary Recipient Mismatch \n"

    

    #primary recipient duplicated within
    PRDW = "SELECT * FROM PrimaryRecipientduplicatedWithin WHERE ProgrammeNo =  %s" 
    PRDWpgno = (pgno, )
    mycursor.execute(PRDW, PRDWpgno)
    myresult4 = mycursor.fetchall()

    if len(myresult4) >= 1:
        ReasonForException +=  "Primary Recipient Duplicated Within \n"

    #primary recipient duplicated across
    PRDA = "SELECT * FROM PrimaryRecipientduplicatedacross WHERE ProgrammeNo =  %s" 
    PRDApgno = (pgno, )
    mycursor.execute(PRDA, PRDApgno)
    myresult5 = mycursor.fetchall()

    if len(myresult5) >= 1:
        ReasonForException +=  "Primary Recipient Duplicated Across \n"

    #Primary Recipient Missing or Ineligible
    PRMOI = "SELECT * FROM PrimaryRecipientMissingOrIneligible WHERE ProgrammeNo =  %s" 
    PRMOIpgno = (pgno, )
    mycursor.execute(PRMOI, PRMOIpgno)
    myresult6 = mycursor.fetchall()

    if len(myresult6) >= 1:
        ReasonForException +=  "Primary Recipient Missing or Ineligible \n"  

    #Secondary Recipient Duplicated Within
    SRDW = "SELECT * FROM SecondaryRecipientduplicatedWithin WHERE ProgrammeNo =  %s" 
    SRDWpgno = (pgno, )
    mycursor.execute(SRDW, SRDWpgno)
    myresult7 = mycursor.fetchall()

    if len(myresult7) >= 1:
        ReasonForException +=  "Seconadary recipient duplicated within \n" 

    #Secondary Recipient IPRS Mismatch
    SRIM = "SELECT * FROM SecondaryRecipientIPRSMismatch WHERE ProgrammeNo =  %s" 
    SRIMpgno = (pgno, )
    mycursor.execute(SRIM, SRIMpgno)
    myresult8 = mycursor.fetchall()

    if len(myresult8) >= 1:
        ReasonForException +=  "Seconadary recipient IPRS Mismatch \n"  

    #Secondary Recipient Duplicated Across
    SRDW = "SELECT * FROM SecondaryRecipientDuplicatedacross WHERE ProgrammeNo =  %s" 
    SRDWpgno = (pgno, )
    mycursor.execute(SRDW, SRDWpgno)
    myresult9 = mycursor.fetchall()

    if len(myresult9) >= 1:
        ReasonForException +=  "Seconadary recipient duplicated Across \n" 

    #SecondaryRecipientMissing
    SRM = "SELECT * FROM SecondaryRecipientMissing WHERE ProgrammeNo =  %s" 
    SRMpgno = (pgno, )
    mycursor.execute(SRM, SRMpgno)
    myresult10 = mycursor.fetchall()

    if len(myresult10) >= 1:
        ReasonForException +=  "Secondary recipient missing \n" 

    #Householdsuspended   
    HHS = "SELECT * FROM Householdsuspended WHERE ProgrammeNo =  %s" 
    HHSpgno = (pgno, )
    mycursor.execute(HHS, HHSpgno)
    myresult11 = mycursor.fetchall()

    if len(myresult11) >= 1:
        ReasonForException +=  "Household Suspended \n" 

    #DormantAccount 
    DA = "SELECT * FROM DormantAccount WHERE ProgrammeNo =  %s" 
    DApgno = (pgno, )
    mycursor.execute(DA, DApgno)
    myresult12 = mycursor.fetchall()

    if len(myresult12) >= 1:
        ReasonForException +=  "Dormant Account \n" 

    #SuspiciousPayment  
    SP = "SELECT * FROM SuspiciousPayment WHERE ProgrammeNo =  %s" 
    SPpgno = (pgno, )
    mycursor.execute(SP, SPpgno)
    myresult13 = mycursor.fetchall()

    if len(myresult13) >= 1:
        ReasonForException +=  "Suspicious Payment \n"  

    if ReasonForException != None:
        return ReasonForException
    else:
        return ("Most likely not in programme. Use CCTPMIS to reconfirm the beneficiary")


#Query the exceptions table 
def query_exceptions(update, context):
    gettgid(update,context)
    verifyuser(userid)
    if status == True:
        pgno = context.args[0]
        update.message.reply_text(EXCEPTIONS(pgno))
    else:
        update.message.reply_text("You are not a verified user")

#login function
def login(email, password):

    mydb = mysql.connector.connect(
    host="192.168.64.2",
    user="deh",
    password="1234",
    database="CCTP"
    )

    mycursor = mydb.cursor()

    #compare email and password
    sql = "SELECT * FROM users WHERE email=%s AND password =%s "
    users = (email,password)
    mycursor.execute(sql,users)
    result = mycursor.fetchall()

    if len(result)>0:
        for x in result:
            user_data = {
                "user_identity": x[0],
                "user_email": x[1],
                "user_password" : x[2]
            }
            token = jwt.encode(
                payload = user_data,
                key = "SECRET"
            )
            global user_token
            user_token = token
            verify(user_token)
            return "You are now loggedin to Inua Jamii Telegram Bot. Proceed to query any information"
    else:
        return "User does not exist"

def verify(user_token):

    try:
        payload = jwt.decode(
            user_token,
            key="SECRET",
            algorithms = ['HS256',]
        )
    except:
        return "Please login again. Your session has expired"

def query_login(update, context):
    email = context.args[0]
    password = context.args[1]
    update.message.reply_text(login(email,password))

def gettgid(update, context):
    user = update.message.from_user
    global userid
    userid = user['id']
    return userid

def verifyuser(telegramid):
    mydb = mysql.connector.connect(
    host="192.168.64.2",
    user="deh",
    password="1234",
    database="CCTP"
    )

    mycursor = mydb.cursor()

    #compare email and password
    sql = "SELECT * FROM tgid WHERE tgid = %s "
    telegramid = (telegramid,)
    mycursor.execute(sql,telegramid)
    result = mycursor.fetchall()

    if len(result) < 1:
        global status 
        status = False
    else:
        status = True
    
    return status

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
#CTOVC query
disp.add_handler(telegram.ext.CommandHandler("ctovc", query_ctovc))
#PWSD query
disp.add_handler(telegram.ext.CommandHandler("pwsd", query_pwsd))
#opct query
disp.add_handler(telegram.ext.CommandHandler("opct", query_opct))
#exceptions query
disp.add_handler(telegram.ext.CommandHandler("exceptions", query_exceptions))
#login
disp.add_handler(telegram.ext.CommandHandler("login", query_login))
#tgid
disp.add_handler(telegram.ext.CommandHandler("tgid", gettgid))
#handle random messages
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
#disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, query_ctovc))
#disp.add_handler(telegram.ext.CommandHandler("ctovc", query_ctovc()))

updater.start_polling()
updater.idle()