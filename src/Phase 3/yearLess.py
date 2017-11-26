from bsddb3 import db



def yearSearch(Ending_Year):

    DB_File = "ye.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()

    middleSet = set()
    result = curs.first()
   # result = curs.set_range(str(Starting_Year).encode("utf-8"))

    if(result != None):
          while(result != None):
            if(str(result[0].decode("utf-8")[0:len(str(Ending_Year))])>=str(Ending_Year)):
                break

            middleSet.add(str(result[1].decode("utf-8")))

    else:
        print("No result was found")
        return ()

    curs.close()
    database.close()
    return middleSet

def main():
    print(yearSearch(1995))


if __name__ == "__main__":
    main()
