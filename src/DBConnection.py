import pymysql
import json


class DBConnection:
    def __init__(self):
        """Generate DB connection"""
        db_config = json.loads(open('../env/db_config.json', 'r').read())
        self.connection = pymysql.connect(host=db_config['host'],
                                          port=db_config['port'],
                                          db=db_config['db'],
                                          user=db_config['user'],
                                          passwd=db_config['passwd'],
                                          autocommit=True,
                                          charset='utf8'
                                          )

    def __del__(self):
        """Disconnect DB"""
        self.connection.close()

    def get_connection(self):
        return self.connection
