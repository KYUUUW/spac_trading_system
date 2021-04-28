import pymysql
db_config = json.loads(open('../env/db_config.json', 'r').read())
connection = pymysql.connect(host=db_config['host'],
                             port=db_config['port'],
                             db=db_config['db'],
                             user=db_config['user'],
                             passwd=db_config['passwd'],
                             autocommit=True,
                             charset='utf8'
                             )