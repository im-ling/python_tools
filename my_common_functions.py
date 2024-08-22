import os
import json
import shutil

def read_text_file_to_lines(file_path):
    file_obj = open(file_path, "r")
    lines = file_obj.readlines()
    file_obj.close()
    return lines


def write_lines_to_path(lines, path):
    with open(path, 'w') as filehandle:
        for line in lines:
            filehandle.write(line)


def all_files_in_folder(folder_path):
    result = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            result.append(file_path)
    return result


def find_all_file_endswith(suffix, local_path):
    result = []
    for root, dirs, files in os.walk(local_path):
        for file in files:
            if file.endswith(suffix):
                file_path = os.path.join(root, file)
                result.append(file_path)
    return result

def delete_file_and_folder(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)

def get_file_name_from_path(path):
    if "/" not in path:
        return path
    result = path.split("/")
    return result[len(result) - 1]


# 使用文件修改时间戳排序，最新的在最后
def sort_files_by_modify_time(file_paths):
    def sort_compare(path):
        return os.path.getmtime(path)
    return sorted(file_paths, key=sort_compare)


# list文件dump成json，添加list元素
def insert_to_listfile(index,item, list_file_path):
    list = []
    if (os.path.isfile(list_file_path)):
        with open(list_file_path, 'r') as openfile:
            # Reading from json file
            list = json.load(openfile)
    list.insert(index, item)
    json_object = json.dumps(list, indent=4)
    with open(list_file_path, "w") as outfile:
        outfile.write(json_object)    

# list文件dump成json，添加list元素， 末尾
def append_to_listfile(item, list_file_path):
    list = []
    if (os.path.isfile(list_file_path)):
        with open(list_file_path, 'r') as openfile:
            # Reading from json file
            list = json.load(openfile)
    list.append(item)
    json_object = json.dumps(list, indent=4)
    with open(list_file_path, "w") as outfile:
        outfile.write(json_object)


# list文件dump成json，添加list元素
def insert_to_dicfile(key, value, dic_file_path):
    dic = {}
    if (os.path.isfile(dic_file_path)):
        with open(dic_file_path, 'r') as openfile:
            # Reading from json file
            dic = json.load(openfile)
    dic[key] = value
    json_object = json.dumps(dic, indent=4)
    with open(dic_file_path, "w") as outfile:
        outfile.write(json_object)   

def valid_str(input):
    if input and type(input) == str and input.strip() != "":
        return True
    return False

def input_replacement(input, old, new):
    if not input:
        return input
    if type(input) == str:
        return input.replace(old, new)
    elif type(input) == list:
        for idx, ele in enumerate(input):
            input[idx] = input_replacement(ele, old, new)
    elif type(input) == dict:
        for key, value in input.items():
            input[key] = input_replacement(value, old, new)
    return input