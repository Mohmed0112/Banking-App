import mysql.connector


def get_cust_info(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='thebank',
                                             user='root',
                                             password='fakepassword')

        cursor = connection.cursor()
        sql_select_query = """select * from thebankinfo where UserID = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()

        full_info = []
        for row in record:
            full_info.append(row[0])
            full_info.append(row[1])
            full_info.append(row[2])
            full_info.append(row[3])
            return full_info

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

def upd_cust_info(id, bal):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='thebank',
                                             user='root',
                                             password='M@3kH032205!')

        cursor = connection.cursor()
        sql_select_query = ('''
                UPDATE thebankinfo
                SET balance = %s
                WHERE userID = %s
                ''')
        # set variable in query
        cursor.execute(sql_select_query, (id, bal))
        connection.commit

        
            

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

cust_info = get_cust_info(int(input("Enter user id: ")))
