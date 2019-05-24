import hashlib
from global_var import SYSTEM_TYPE

class FileInfo:
    __name = str()
    __base_path = str()
    __relative_path = str()
    __path = str()
    __hash_id = str()
    __isFolder = bool()
    __size = str()
    __modify_time = str()

    def __init__(self, name, isFolder, modify_time, hash_id=None, base_path=None, relative_path=None, size='0KB'):
        if type(name) != str:
            raise RuntimeError('The name must be a string type')
        if type(base_path) != str and base_path != None:
            raise RuntimeError('The base_path must be a string type')
        if type(relative_path) != str and relative_path != None:
            raise RuntimeError('The relative_path must be a string type')
        if type(isFolder) != bool:
            raise RuntimeError('The isFolder must be a bool type')
        if type(size) != str:
            raise RuntimeError('The size must be a string type')
        if type(modify_time) != str:
            raise RuntimeError('The modify time must be a string type')
        if type(hash_id) != str and hash_id != None:
            raise RuntimeError('The hash id must be a string type!')

        self.__name = name
        self.__relative_path = relative_path
        self.__base_path = base_path
        self.__isFolder = isFolder
        self.__size = size
        self.__modify_time = modify_time

        if base_path != None and relative_path != None:
            self.__path = base_path + relative_path;
        
        if hash_id != None:
            self.__hash_id = hash_id
        elif self.__path != None:
            h = hashlib.md5()
            h.update(self.__path.encode('utf8'))
            self.__hash_id = h.hexdigest()

    def getName(self) -> str:
        return self.__name

    def getPath(self) -> str:
        if self.__path != None:
            if SYSTEM_TYPE == 'Windows':
                return self.__path.replace('/', '\\')
        else:
            raise RuntimeError('The path not set!')

    def getIsFolder(self) -> bool:
        return self.__isFolder
    
    def getSize(self) -> str:
        return self.__size

    def getHash(self) -> str:
        return self.__hash_id

    def getRelativePath(self) -> str:
        return self.__relative_path

    def getBasePath(self) -> str:
        return self.__base_path

    def getModifyTime(self) -> str:
        return self.__modify_time

    def setFullPath(self, fullPath):
        if type(fullPath) != str:
            raise RuntimeError('The fullpath must be str type!')

        self.__path = fullPath