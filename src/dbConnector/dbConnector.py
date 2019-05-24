import pymysql
import hashlib
import time
import os
from src.dbConnector.FileInfo import FileInfo
from global_var import SYSTEM_TYPE

class dbConnector:
    'The class is used to establish connection between the database and the appliction'
    __db_obj = object()
    __db_cursor = object()
    __host_name = str()
    __db_usr_name = str()
    __db_pwd = str()

    # public method here
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

    def walk_path(self):
        if SYSTEM_TYPE == "Windows":
            self.__windows_walk_path()
        elif SYSTEM_TYPE == "MacOS":
            self.__macOS_walk_path()

    'Destructor, to close the connection and commit all'
    def __del__(self):
        self.__db_cursor.commit()
        self.__db_cursor.close()
        self.__db_obj.close()

    def insert_file_obj(self, file_info_obj):
        if type(file_info_obj) != FileInfo:
            raise RuntimeError('The file_info_obj must be a FileInfo Object!')

        self.__insert_single_file(file_info_obj.getBasePath(), file_info_obj.getRelativePaht(),
                                file_info_obj.getName(), file_info_obj.getModifyTime(),
                                file_info_obj.getModifyTime(), file_info_obj.getSize(),
                                file_info_obj.getIsFolder())

    def search_file(self, file_name) -> list:
        self.__search_file(file_name)
        return __fetch_file_info()

    def setFileFullPath(self, file):
        if type(file) != FileInfo:
            raise RuntimeError('The file must be a FileInfo type')

        sql = "call getFullPath('{}')".format(file.getHash)
        self.__db_cursor.execute(sql)
        temp = self.__db_cursor.fetchall()

        name_list = list()
        for line in temp:
            t = line
            name_list.append(t)

        fullPath = ''
        for name in name_list:
            fullPath += name + '/'

        file.setFullPath(fullPath)


    # private method here
    def __windows_walk_path(self):
        # To search how many disk the system has
        disk_list = []
        char_list = [chr(i) for i in range(65, 91)]
        for char in char_list:
            if os.path.isdir(char + ':\\'):
                disk_list.append(char)
        
        for disk in disk_list:
            g = os.walk(disk + ':\\')
            for path, dir_list, file_list in g:
                for dir_name in dir_list:
                    full_path = os.path.join(path, dir_name)
                    statinfo = os.stat(path)
                    local = time.localtime(statinfo.st_ctime)
                    modify_time = str(local.tm_year) 
                    + '-' + str(local.tm_mon) 
                    + '-' + str(local.tm_mday) 
                    + ' ' + str(local.tm_hour) 
                    + ':' + str(local.tm_min) 
                    + ':' + str(local.tm_sec)

                    size = str(statinfo.st_size / 1024) + 'KB'
                    f = FileInfo(dir_name, True, modify_time)



    def __macOS_walk_path(self):
        return None

    def __search_file(self, file_name):
        sql = "select * from file_info where name = '{}'".format(file_name)
        self.__db_cursor.execute(sql)

    'Return the file info object list in the cache'
    def __fetch_file_info(self) -> list:
        temp = __db_cursor.fetchall()
        file_list = list()
        hash_id = str()
        name = str()
        modify_time = str()
        size = str()
        isFolder = bool()
        pre_folder_id = str()

        for line in temp:
            hash_id, name, modify_time, size, isFolder, pre_folder_id = line
            file_list.append(FileInfo(name, isFolder, modify_time, hash_id, size=size))

        return file_list

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
    def __insert_single_file(self, hash_id, name, modify_time, size, isFolder=True):
        if type(hash_id) != str:
            raise RuntimeError('The hash_id must be a string type!')
        # if type(relative_path) != str:
        #     raise RuntimeError('The relative_path must be a string type!')

        # current_path = str()
        # current_path = base_dir + relative_path
        # h = hashlib.md5()
        # h.update(current_path.encode('utf8'))
        current_path_id = hash_id
        value_list = [current_path_id, name, str(modify_time), size, str(isFolder)]

        try:
            self.__insert_info('file_info', value_list)
            __db_obj.commit()
        except Exception as e:
            __db_obj.rollback()
            raise Exception(e)