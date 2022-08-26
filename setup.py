# !/use/bin/env python

'''
:$sudo pip install Cython
'''
import sys
sys.dont_write_bytecode = True
from setuptools import setup
from Cython.Build import cythonize
import configHelper
import cmdHelper as cmd

configHelper.read_config_ini()

def main():

    # onoff iterate file list.(Used python3.8 setup.py build_ext)
    if configHelper.config_dict['file_path_list']:
        for key in configHelper.global_dict:
            print(key)
            print(configHelper.global_dict[key])

            # Path to encrypte files to .so by assign .py absolute file path.
            dst_encrypt_path = configHelper.getFileFullPath(key)

            # enryption .py file to .so file.
            setup(
                name=key,
                ext_modules=cythonize([dst_encrypt_path])
            )

            # move .so file to correspond location.
            cmd.delDotCFile(key)
            # Rename the original .so file to assign .so name.
            cmd.renameDotSoFile(key)
            # Remove original file.
            cmd.removeFile(key)
            # Move .so to right place.
            cmd.moveFile(key)

    else:
        # single file encryption by manual setting. (Used python3.8 setup.py build_ext --inplace)
        filename = 'deviceService.py'

        # enryption .py file to .so file.
        setup(
            ext_modules=cythonize(['./' + filename])
        )

        # move .so file to correspond location.
        cmd.delDotCFile(filename)
        # Rename the original .so file to assign .so name.
        cmd.renameDotSoFile(filename)
        # Remove original file.
        cmd.removeFile(filename)
        # Move .so to right place.
        cmd.moveFile(filename)

    print('=========== Finish encryption!!! ===========')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

