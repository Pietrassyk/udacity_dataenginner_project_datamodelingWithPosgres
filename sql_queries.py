# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
songplay_id SERIAL PRIMARY KEY, 
start_time BIGINT, 
user_id INT, 
level TEXT, 
song_id TEXT, 
artist_id TEXT, 
session_id INT, 
location TEXT, 
user_agent TEXT)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
user_id INT, 
first_name TEXT, 
last_name TEXT, 
gender TEXT, 
level TEXT
)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
song_id TEXT,
title TEXT,
artist_id TEXT,
year INT,
duration FLOAT
)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
artist_id TEXT,
name TEXT,
location TEXT,
latitude FLOAT,
longitude FLOAT
)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
start_time BIGINT,
hour INT,
day INT,
week INT,
month INT,
year INT,
weekday TEXT
)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (
start_time, 
user_id, 
level, 
song_id, 
artist_id, 
session_id, 
location, 
user_agent) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""SELECT s.song_id
                        , a.artist_id
                    FROM artists a
                    INNER JOIN songs s
                    ON a.artist_id = s.artist_id
                    WHERE s.title = %s
                    AND a.name = %s
                    AND s.duration = %s
                            """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]