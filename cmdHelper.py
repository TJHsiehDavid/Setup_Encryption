import os
import shutil
import configHelper as ch


filePath3 = '/build'
full_path = None

def delDotCFile(filename):
    # .py檔的當前目錄
    if ch.config_dict['file_path_list']:
        path = ch.sdk_dir + filePath3 + ch.global_dict[filename]
    else:
        path = ch.sdk_dir + '/'
    # list全部檔案底下的文件
    files = os.listdir(path)
    for file in files:
        if file.endswith(".c"):
            # 判斷檔案是否存在
            if (os.path.exists(path + file)):
                os.remove(path + file)
                print('移除 ' + file + ' success!')
            else:
                print("要刪除的檔案不存在！")


def renameDotSoFile(filename):
    global full_path
    # .so檔的當前目錄 = setup.py這加密執行檔的當前路徑
    build_path = os.path.dirname(os.path.abspath(__file__)) + filePath3
    # list全部檔案底下的文件
    file_under_build = os.listdir(build_path)
    for home_dir in file_under_build:
        if home_dir.split('.')[0] == 'lib':
            full_path = build_path + '/' + home_dir + '/'
    # default full abs path
    if full_path is None:
        full_path = build_path + '/' + 'lib.linux-x86_64-3.8' + '/'
    files = os.listdir(full_path)

    # 修改原本.so檔的檔名.
    for file in files:
        if file.endswith(".so") and ('cpython' in file):
            # 判斷檔案是否存在
            if (os.path.exists(full_path + file)):
                src_file = full_path + file
                dst_file = full_path + file.split('.')[0] + '.so'
                os.rename(src_file, dst_file)
                print('修改 ' + file + ' success!')
            else:
                print("要修改的檔案不存在！")


def moveFile(filename):
    so_filename = filename.split('.')[0] + '.so'
    # 判斷檔案是否存在
    if (os.path.exists(full_path + so_filename)):
        src_file = full_path + so_filename
        dst_file = ch.sdk_dir + filePath3 + ch.global_dict[filename]
        if (os.path.exists(dst_file + so_filename)):
            removeFile(so_filename)
        shutil.move(src_file, dst_file)
        print('move ' + so_filename + ' success!')
    else:
        print("要move的檔案不存在！")


def removeFile(filename):
    py_filename = filename.split('.')[0] + '.py'
    so_filename = filename.split('.')[0] + '.so'
    file_Path = ch.sdk_dir + filePath3 + ch.global_dict[py_filename]
    if (os.path.exists(file_Path + py_filename)):
        os.remove(file_Path + py_filename)
        print('remove ' + file_Path + py_filename + ' success!')
    else:
        print("要remove的檔案 " + py_filename + " 不存在！")

    if (os.path.exists(file_Path + so_filename)):
        os.remove(file_Path + so_filename)
        print('remove ' + file_Path + so_filename + ' success!')
    else:
        print("要remove的檔案 " + so_filename + " 不存在！")