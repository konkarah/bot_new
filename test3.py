import jwt
import json
from jwt.exceptions import ExpiredSignatureError
import mysql.connector

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
            #return "You are now loggedin to Inua Jamii Telegram Bot. Proceed to query any information"
    else:
        print ("User does not exist")

def verify(user_token):

    try:
        payload = jwt.decode(
            user_token,
            key="SECRET",
            algorithms = ['HS256',]
        )
        print(payload)
    except:
        print ("Please login again. Your session has expired")


login("itsthindi@gmail.com", "1234")
verify(user_token)