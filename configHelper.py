import os
from configparser import ConfigParser

sdk_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(sdk_dir)

global_dict = {}
config_dict = {}

def write_config_ini(self):
    #sdk_dir = os.path.dirname(os.path.abspath(__file__))
    config = ConfigParser()
    config.read(sdk_dir + '/fileConfig.ini')

    hd = open(sdk_dir + '/fileConfig.ini', "w")
    config.write(hd)
    hd.close()

def read_config_ini():
    #sdk_dir = os.path.dirname(os.path.abspath(__file__))
    file_config = ConfigParser()
    # -----------加上這下面一行就可以區分大小寫-----------
    file_config.optionxform = str

    file_config.read(sdk_dir + '/fileConfig.ini')

    # Read ini index info
    FILE_PATH_LIST = int(file_config['Setting']['file_path_list'])
    config_dict['file_path_list'] = FILE_PATH_LIST
    print('FILE PATH LIST: ', 'yes' if FILE_PATH_LIST else 'no')


    # File path list dictionary.
    path_list = file_config.items("file_path_list")
    for key, val in path_list:
        print("read_config_ini key:" + str(key) + " val:" + str(val))
        global_dict[str(key)] = str(val)


def set_value(self, name, value):
    global_dict[name] = value

def get_value(self, name, defValue=None):
    try:
        return global_dict[name]
    except KeyError:
        return defValue

def getFileFullPath(filename):
    return sdk_dir + '/build' + global_dict[filename] + filename