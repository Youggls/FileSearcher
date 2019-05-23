import pymysql

class dbConnector:
    'The class is used to establish connection between the database and the appliction'
    __db_obj = object()
    __db_cursor = object()
    __host_name = str()
    __db_usr_name = str()
    __db_pwd = str()

    '''
    The init function
    The frist arg is the database's adderss, 'localhost' or 'example.com' or '0.0.0.0'
    The second arg is the database's user name
    The third arg is the database's password
    The last arg is the databases's default schema
    They must be string type!
    '''
    def __init__(self, host_name, db_usr, db_pwd, default_schema):
        if type(host_name) != str:
            raise RuntimeError('The host_name must be a string type!')
        if type(db_usr) != str:
            raise RuntimeError('The db_usr must be a string type!')
        if type(db_pwd) != str:
            raise RuntimeError('The db_pwd must be a string type!')
        if type(default_schema) != str:
            raise RuntimeError('The defalut_schema must be a string type!')

        __db_obj = pymysql.connect(host_name, db_usr, db_pwd, default_schema)
        __db_cursor = __db_obj.cursor()
        __host_name = host_name
        __db_usr_name = db_usr
        __db_pwd = db_pwd

    'return the cache info from the cursor object'
    def fecth_info(self):
        return __db_cursor.fetchall()