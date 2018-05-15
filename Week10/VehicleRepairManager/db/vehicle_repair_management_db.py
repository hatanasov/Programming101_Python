import sqlite3

DB_NAME = "vehicle_repair_management.db"

db = sqlite3.connect(DB_NAME)
c = db.cursor()

tables = ("base_user", "client")
drop_tables = """DROP TABLE IF EXISTS """

for table in tables:
    c.execute(drop_tables + table)

table_baseuser = """
CREATE TABLE IF NOT EXISTS base_user (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_NAME TEXT UNIQUE NOT NULL ,
    EMAIL TEXT UNIQUE NOT NULL ,
    PHONE_NUMBER INTEGER UNIQUE NOT NULL ,
    ADDRESS TEXT NOT NULL
)
"""

c.execute(table_baseuser)
db.commit()

table_client = """
CREATE TABLE IF NOT EXISTS client (
    BACE_ID INTEGER,
    FOREIGN KEY(BACE_ID) REFERENCES BACE_ID(ID)
)   
"""

c.execute(table_client)
db.commit()


table_vehicle = """
CREATE TABLE IF NOT EXISTS vehicle (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CATEGORY TEXT NOT NULL,
    MAKE TEXT NOT NULL,
    MODEL TEXT NOT NULL,
    REGISTER_NUMBER TEXT UNIQUE NOT NULL,
    GEAR_BOX TEXT NOT NULL, 
    OWNER INTEGER, 
    FOREIGN KEY(OWNER) REFERENCES BASE_USER(ID)
)
"""

c.execute(table_vehicle)
db.commit()
# insert_user = """
# INSERT INTO base_user (user_name, email, phone_number, address)
#     VALUES ('hristo', 'hristo@gmail.com', 0888123, 'Sofia')
# """

# c.execute(insert_user)
# db.commit()

db.close()
