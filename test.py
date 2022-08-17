import mysql.connector

def ctvc(pgno):
    mydb = mysql.connector.connect(
    host="192.168.64.2",
    user="deh",
    password="1234",
    database="CCTP"
    )

    mycursor = mydb.cursor()

    sql = "SELECT BankName,BranchName,AccountName,Amount FROM table_name WHERE ProgrammeNO = %s"
    pgno = (pgno, )

    mycursor.execute(sql, pgno)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
ctvc(1010488)