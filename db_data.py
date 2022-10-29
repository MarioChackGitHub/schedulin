import pymysql
from sqlalchemy import create_engine
from datetime import datetime

user = "MarioTheBridge"
passw = "thebridge1234"
host = "MarioTheBridge.mysql.pythonanywhere-services.com"
database = "MarioTheBridge$schedulin"

db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
conn = db.connect()

now = datetime.now() #te dice la hora local del servidor

timetables_lst = [
    """INSERT INTO timetable (start_time, end_time, creation_date)
           VALUES ('09:00:00', '10:30:00', '{0}')""".format(now),
    """INSERT INTO timetable (start_time, end_time, creation_date)
           VALUES ('10:30:00', '12:00:00', '{0}')""".format(now),
    ]

resources_lst = [
    """INSERT INTO resource (timetable_id, type, description, max_pax, price, hours_in_advance, creation_date)
           VALUES (1, 'PADEL', '', 4, 0.50, 24, '{0}')""".format(now),
    """INSERT INTO resource (timetable_id, type, description, max_pax, price, hours_in_advance, creation_date)
           VALUES (2, 'PADEL', '', 4, 0.50, 24, '{0}')""".format(now),
    ]

users_lst = [
    """INSERT INTO user (name, email, status, creation_date)
           VALUES ('John Doe', 'johndoe@mail.com', 'ACTIVE', '{0}')""".format(now),
    ]

reservations_lst = [
    """INSERT INTO reservation (resource_id, user_id, start_time, num_pax, status, creation_date)
           VALUES (1, 1, '09:00:00', 2, 'CONFIRMED', '{0}')""".format(now),
    ]

inserts_lst = [timetables_lst, resources_lst,
    users_lst, reservations_lst]

for lst in inserts_lst:
    for t in lst:
        print(t)
        conn.execute(t)

conn.close()



SELECT r.type as resource_type,

FROM (
    SELECT type
    FROM resource) AS r
LEFT JOIN (
    SELECT id, name, email
    FROM user) AS u
ON r.user_id = u.id;



#Para seleccionar name, type, start_time, end_time:
SELECT
	r.id AS reservation_id,
	r.status AS reservation_status,
	r.date,
	u.name AS user_name,
	u.email AS user_email,
	re.type AS resource_type,
	re.price AS price,
	t.start_time,
	t.end_time

FROM (
	SELECT id, status, user_id, resource_id, date
	FROM reservation) AS r
LEFT JOIN (
	SELECT id, name, email
	FROM user) AS u
ON r.user_id = u.id
LEFT JOIN (
	SELECT id, type, price, timetable_id
	FROM resource) AS re
ON r.resource_id = re.id
LEFT JOIN (
	SELECT id, start_time, end_time
	FROM timetable) as t
ON re.timetable_id = t.id;


#Updatear la tabla reservation para que se actualiza la fecha:
UPDATE reservation
SET date = '2022-10-31'
WHERE id = 1;  #porque solo me interesa que la actualización sea en la reserva 1








