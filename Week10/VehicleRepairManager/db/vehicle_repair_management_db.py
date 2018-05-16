import sqlite3

DB_NAME = "vehicle_repair_management.db"

db = sqlite3.connect(DB_NAME)
c = db.cursor()

tables = ("base_user", "client", "vehicle",
          "mechanic", "mechanic_services", "service", "vehicle_repair")

drop_tables = """DROP TABLE IF EXISTS """

for table in tables:
    c.execute(drop_tables + table)

db.commit()

table_base_user = """
CREATE TABLE IF NOT EXISTS base_user (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_NAME TEXT UNIQUE NOT NULL ,
    EMAIL TEXT UNIQUE ,
    PHONE_NUMBER INTEGER UNIQUE NOT NULL ,
    ADDRESS TEXT NOT NULL
)
"""

table_client = """
CREATE TABLE IF NOT EXISTS client (
    BASE_ID INTEGER,
    FOREIGN KEY (BASE_ID) REFERENCES BASE_USER(ID)
)   
"""

table_vehicle = """
CREATE TABLE IF NOT EXISTS vehicle (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CATEGORY TEXT NOT NULL,
    MAKE TEXT NOT NULL,
    MODEL TEXT NOT NULL,
    REGISTER_NUMBER TEXT UNIQUE NOT NULL,
    GEAR_BOX TEXT NOT NULL, 
    OWNER INTEGER NOT NULL, 
    FOREIGN KEY(OWNER) REFERENCES CLIENT(BASE_ID)
)
"""


table_mechanic = """
CREATE TABLE IF NOT EXISTS mechanic (
    BASE_ID INTEGER,
    TITLE TEXT NOT NULL,
    FOREIGN KEY (BASE_ID) REFERENCES BASE_USER(ID)
)
"""

table_mechanic_services = """
CREATE TABLE IF NOT EXISTS mechanic_service (
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    MECHANIC_ID INTEGER NOT NULL,
    SERVICE_ID INTEGER NOT NULL,
    FOREIGN KEY (MECHANIC_ID) REFERENCES MECHANIC(BASE_ID),
    FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(ID)
)
"""

table_service = """
CREATE TABLE IF NOT EXISTS service (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT UNIQE NOT NULL
)
"""

table_vehicle_repair = """
CREATE TABLE vehicle_repair (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    start_hour TEXT NOT NULL,
    vehicle INTEGER UNIQE NOT NULL,
    bill REAL NOT NULL,
    mechanic_service INTEGER UNIQE NOT NULL,
    FOREIGN KEY (vehicle) REFERENCES vehicle(ID),
    FOREIGN KEY (mechanic_service) REFERENCES mechanic_service(id)
)
"""

create_table = (table_base_user, table_client, table_vehicle,
                table_mechanic, table_mechanic_services, table_service, table_vehicle_repair)

for table in create_table:
    c.execute(table)

db.commit()

db.close()
