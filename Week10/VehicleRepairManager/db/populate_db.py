import sqlite3

DB_NAME = "vehicle_repair_management.db"

db = sqlite3.connect(DB_NAME)
c = db.cursor()

base_user_client = [(5, 'Hristo', 'hristo@gmail.com', '088123', 'Sofia'),
                    (6, 'Poli', 'poli@yahoo.com', '0898234', 'Montana'),
                    (7, 'Sasho', 'sasho_123@abv.bg', '088345', 'Plovdiv')
                    ]

client_id = [('5'),
             ('6'),
             ('7')
             ]

vehicle = [(1, 'Car', 'fiat', 'punto', 'CT543', 'manual', 5),
           (2, 'Motorcycle', 'kawazaki', 'ninja', 'C1231', 'feet', 6),
           (3, 'Buggy car', 'buggy', 'home made', 'unregistrated', 'manual', 7)
           ]

vehicle_repair = [('2018-05-20', '9:00', 1, 150, 1),
                  ('2018-05-20', '10:00', 2, 80, 2),
                  ('2018-05-20', '11:00', 3, 400, 3)
                  ]

base_user_mechanic = [(1, 'Ivo', 'ivo@cs.com', '0778123', 'Sofia'),
                      (2, 'Joro', 'joro@cs.com', '0778124', 'Sofia'),
                      (3, 'Pepi', 'pepi@cs.com', '077125', 'Sofia'),
                      (4, 'Mecho', 'mecho@cs.com', '077126', 'Sofia')
                      ]

mechanic = [('1', 'engines'),
            ('2', 'electrics'),
            ('3', 'brakes and suspension'),
            ('4', 'motorcycles')
            ]

mechanic_service = [(1, 3, 2),
                    (2, 4, 3),
                    (3, 1, 1)
                    ]

service = [(1, 'change oil and filters'),
           (2, 'suspension repair'),
           (3, 'starter repair'),
           (4, 'tires change')
           ]

add_base_user = """
INSERT INTO base_user (id, user_name, email, phone_number, address)
    VALUES (?, ?, ?, ?, ?)
"""


add_id_in_client_table = """
INSERT INTO client (BASE_ID)
    VALUES (?)
"""

add_mechanic_title = """
INSERT INTO mechanic (BASE_ID, TITLE)
    VALUES (?, ?)
"""

add_car_to_vehicle_table = """
INSERT INTO vehicle (ID, CATEGORY, MAKE, MODEL, REGISTER_NUMBER, GEAR_BOX, OWNER)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""

add_vehicle_repair = """
INSERT INTO vehicle_repair (DATE, START_HOUR, VEHICLE, BILL, MECHANIC_SERVICE)
    VALUES (?, ?, ?, ?, ?)
"""

add_mechanic_service = """
INSERT INTO mechanic_service (ID, MECHANIC_ID, SERVICE_ID)
    VALUES (?, ?, ?)
"""

add_service = """
INSERT INTO service (ID, NAME)
    VALUES (?, ?)
"""

try:
    c.executemany(add_base_user, base_user_mechanic)
    c.executemany(add_base_user, base_user_client)
    c.executemany(add_id_in_client_table, client_id)
    c.executemany(add_mechanic_title, mechanic)
    c.executemany(add_car_to_vehicle_table, vehicle)
    c.executemany(add_vehicle_repair, vehicle_repair)
    c.executemany(add_mechanic_service, mechanic_service)
    c.executemany(add_service, service)
except Exception as e:
    print("""All or some tables are populated yet.
Try to renew tables with starting <vehicle_repair_management_db.py> script,
then populate them again.
""")
    db.rollback()
else:
    (print("All tables are populated."))
    db.commit()


db.close()
