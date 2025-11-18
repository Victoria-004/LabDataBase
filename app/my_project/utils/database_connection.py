import mysql.connector
import yaml

def get_db_config():
    with open('app/config/app.yml', 'r') as f:
        config = yaml.safe_load(f)
    return config['mysql']

def get_db_connection():
    config = get_db_config()
    config['charset'] = 'utf8mb4'
    config['collation'] = 'utf8mb4_unicode_ci'
    return mysql.connector.connect(**config)