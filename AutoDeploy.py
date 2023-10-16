"""

Copy code to the target folder

"""

import shutil
import os
# import glob
import datetime
import time

# ==================================================================================================================

# Add code to update
MIAN_CODE = """
XXXX/SOURCE_FOLDER
XXXX/SOURCE_FILE.md
#XXXX/IGNORED_FOLDER

"""



# Add traget code path
TARGET_FOLDER = r"""

XXXX/TARGET_FOLDER


"""


SPECIAL_PAIR = """
  |
  |
  | 
"""

# ==================================================================================================================

def copy_code(main_code, source):
    code_list = [x.strip() for x in main_code.split('\n') if x.strip()]
    code_list = [x for x in code_list if not '#' in x]

    source = source.strip().replace('\\', '/')
    source = [x for x in source.split('\n') if not '#' in x][0]
    for code_path in code_list:
        # code_name = os.path.basename(code_path)
        code_name = code_path
        source_path = os.path.join(source, code_name).replace('\\', '/')

        if os.path.isdir(code_path):
            shutil.copytree(code_path, source_path, dirs_exist_ok=True)
        else:
            dir_path = os.path.dirname(source_path)
            os.makedirs(dir_path, exist_ok=True)
            shutil.copy2(code_path, source_path,)
        print('File copied:', source_path)


def main():
    print()
    copy_code(MIAN_CODE, TARGET_FOLDER)


if __name__=='__main__':
    main()
    print(datetime.datetime.now())
    print('Done!')
    time.sleep(10)
