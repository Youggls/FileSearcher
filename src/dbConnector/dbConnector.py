import pymysql
import hashlib
from src.dbConnector.FileInfo import FileInfo

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

    def insert_file_obj(self, file_info_obj):
        if type(file_info_obj) != FileInfo:
            raise RuntimeError('The file_info_obj must be a FileInfo Object!')

        self.__insert_single_file(file_info_obj.getBasePath(), file_info_obj.getRelativePaht(),
                                file_info_obj.getName(), file_info_obj.getModifyTime(),
                                file_info_obj.getModifyTime(), file_info_obj.getSize(),
                                file_info_obj.getIsFolder())

    'insert method, private, please make sure that the table is same with value_list'
    def __insert_info(self, target_table, value_list):
        if type(target_table) != str:
            raise RuntimeError('The target_table must be a string type!')
        if type(value_list) != list:
            raise RuntimeError('The value_list must be a list type!')
        
        sql = "insert into {} values".format(target_table)
        sql += '('
        for index in range(len(value_list)):
            sql += value_list[index]
            if index != len(value_list) - 1:
                sql += ','
        sql += ')'
        self.__db_curosr.execute(sql)

    'insert single_file into database, info includes the name, modify_time, size, isFolder'
    def __insert_single_file(self, base_dir, relative_path, name, modify_time, size, isFolder=True):
        if type(base_dir) != str:
            raise RuntimeError('The base_dir must be a string type!')
        if type(relative_path) != str:
            raise RuntimeError('The relative_path must be a string type!')
        
        current_path = str()
        current_path = base_dir + relative_path
        h = hashlib.md5()
        h.update(current_path.encode('utf8'))
        current_path_id = str(h.hexdigest())
        value_list = [current_path_id, name, str(modify_time), size, str(isFolder)]

        try:
            self.__insert_info('file_info', value_list)
            __db_obj.commit()
        except BaseException as e:
            __db_obj.rollback()
            raise Exception(e)


    'return the file info list'
    def fetch_file_info(self):
        temp_data = __db_cursor.fetchcall();