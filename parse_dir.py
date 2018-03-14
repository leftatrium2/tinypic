# -*- coding: utf-8 -*-
import os


def parse_dir(path, tar_path):
    if path is None:
        return
    if not os.path.exists(path):
        return
    all_file = get_all_files(path, tar_path)
    return all_file


def get_all_files(path, tar_dir_path):
    allfile = {'path': [], 'tar': []}
    # 如果目标文件夹没有，那么就建立一个
    if not os.path.exists(tar_dir_path):
        os.mkdir(tar_dir_path)
    if not os.path.exists(path):
        print("the image path is not exists!!!")
        return
    for dirpath, dirnames, filenames in os.walk(path):
        # for dir in dirnames:
        # allfile.append(os.path.join(dirpath, dir))
        for name in filenames:
            ext_path = os.path.splitext(name)
            if (ext_path[1] == '.png' or ext_path[1] == '.jpg'):
                allfile['path'].append(os.path.join(dirpath, name))
                tar_path = dirpath.replace(path, tar_dir_path)
                allfile['tar'].append(os.path.join(tar_path, name))
    return allfile

# if __name__ == '__main__':
#     files = parse_dir('/Users/sunxiao/Desktop/TestAndroid/app/src/main/res',
#                       '/Users/sunxiao/Desktop/tar')
#     print(files)
