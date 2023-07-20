import os


def get_file_list(source_path):
    file_path_list = []
    file_name = []
    walk = os.walk(source_path)
    for root, dirs, files in walk:
        for name in files:
            filepath = os.path.join(root,name)
            file_name.append(name)
            file_path_list.append(filepath)
    return file_path_list
