import pymysql
import json

db_config = json.loads(open('../env/db_config.json', 'r').read())


def get_connection():
    return pymysql.connect(host=db_config['host'],
                             port=db_config['port'],
                             db=db_config['db'],
                             user=db_config['user'],
                             passwd=db_config['passwd'],
                             autocommit=True,
                             charset='utf8'
                             )
