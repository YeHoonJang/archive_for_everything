import os


CUR_DIR = os.getcwd()

def make_subdir(parent_dir, sub_dir_name):
    try:
        sub_dir = os.path.join(parent_dir, sub_dir_name)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
        return sub_dir
    except:
        pass
        #logging


def is_grant_or_app(name):
    try:
        if 'ipg' in name.split('.')[0]:
            pat_type = 'grants'
            return pat_type
        elif 'ipa' in name.split('.')[0]:
            pat_type = 'applications'
            return pat_type
    except:
        print("ERROR")
        pass
        #logging


def byte_unit_converter(number_of_bytes):
    if number_of_bytes < 0:
        raise ValueError("!!! numberOfBytes can't be smaller than 0 !!!")

    step_to_greater_unit = 1024.

    number_of_bytes = float(number_of_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes) + ' ' + unit


def is_file_download(url_file_size):
    user_answer = input("The file's size is about " + url_file_size + ".\nContinue to download? [y/n] : ")
    flag = True
    while flag:
        if user_answer.upper() in ["Y", "YES"]:
            is_download = True
            flag = False
            return is_download
        elif user_answer.upper() in ["N", "NO"]:
            is_download = False
            flag = False
            return is_download
        else:
            print("Wrong input, Input again.")
            user_answer = input("Continue to download? [y/n] : ")