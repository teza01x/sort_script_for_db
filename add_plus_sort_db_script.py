import sqlite3 as sq


def add_data_to_db(db, data):
    with sq.connect(db) as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO clients VALUES(?,?,?,?)", data)
        con.commit()


def sort_db(db):
    with sq.connect(db) as con:
        cur = con.cursor()
        try:
            data = cur.execute("SELECT * FROM clients")
            result_list = list()
            for i in [j for j in data]:
                if i not in result_list:
                    result_list.append(i)
            cur.execute("DELETE FROM clients")
            cur.executemany("INSERT INTO clients VALUES(?,?,?,?)", result_list)
            con.commit
        except:
            print("We have a mistake!")


if __name__ == "__main__":
    db = "test.db"
    data = [
        ("Andrew Kateman", "andrew@gmail.com", 19, 10000),
        ("Alleson Hungary", "hungarylost@gmail.com", 45, 43000),
        ("Joe Biden", "joeuleran@gmail.com", 34, 31000),
        ("Gandalf Gray", "gg331@gmail.com", 54, 99000),
        ("Terry Huge", "uliras@gmail.com", 49, 112000),
        ("Anita Willson", "anwe@gmail.com", 26, 86000),
        ("Barry Leis", "barrygun@gmail.com", 28, 234000),
        ("Katy Wood", "katyw@gmail.com", 25, 35000),
        ("Jerry Saul", "sauljerry773@gmail.com", 29, 114000),
        ("Vira Lemman", "vira994@gmail.com", 37, 95000),
    ]

    try:
        with sq.connect(db) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS clients(
                        name TEXT,
                        email TEXT,
                        old INTEGER,
                        salary INTEGER
            )""")
    except:
        print("data base clients already created")
    
    for i in range(100):
        add_data_to_db(db, data)

    sort_db(db)
