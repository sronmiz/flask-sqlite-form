DB_PATH = 'subjects_db.sql'
TABLE_NAME = 'subjects'
CREATE_TABLE = f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME}
             (name text, surname text, email text, weight real, height real, feelings int)'''