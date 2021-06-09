import sqlite3
def insertOrUpdate(Id, Name, roll,fe) :                                            # this function is for database
    connect = sqlite3.connect("Face-DataBase")                                  # connecting to the database
    cmd = "SELECT * FROM CSE52 WHERE ID = " + Id                             # selecting the row of an id into consideration
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE CSE52 SET Name = ? WHERE ID = ?",(Name, Id))
        connect.execute("UPDATE CSE52 SET Roll = ? WHERE ID = ?",(roll, Id))
        connect.execute("UPDATE CSE52 SET FaceEncoding = ? WHERE ID = ?",(fe, Id))
    else:
        params = (Id, Name, roll, fe)                                               # insering a new student data
        connect.execute("INSERT INTO CSE52(ID, Name, Roll,FaceEncoding) VALUES(?, ?, ?, ?)", params)
    connect.commit()                                                            # commiting into the database
    connect.close()   

    


