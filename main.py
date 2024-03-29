# -*- coding: utf-8 -*-
from parse_arg import parse_args
from read_config import read_config
from parse_dir import parse_dir
from alloc_tasks import alloc_tasks
import tinify
import sys
import os

__author__ = 'sunxiao'
__copyright__ = 'Copyright 2018, The EllaClub organization'
__license__ = 'BSD'
__version__ = '0.0.1'
__email__ = 'leftatrium@vip.qq.com'


def read_file_list(filepath=''):
    if filepath == '':
        return


# 主函数
if __name__ == '__main__':
    args = {}
    keys = []
    all_files = []
    proxy = ''
    img_list = []
    img_tar_list = []
    remain_num_list = {}
    remain_all_num = 0
    tasks = {}
    # 读取命令行参数
    args = parse_args()
    # 从命令行中读取的目标目录，读取相应的需要处理的文件
    img_dir = args['dict']
    tar_dir = args['target']
    all_files = parse_dir(img_dir, tar_dir)
    img_list = all_files['path']
    img_tar_list = all_files['tar']
    # 从命令行参数中，读取配置文件信息
    config_path = args['conf']
    if not os.path.exists(config_path):
        print("cant find the config path,pls use -c [path] to tell me the true path!!!")
        exit()
    arrs = read_config(config_path)
    keys = arrs['key']
    print("key list:", keys)
    # 读取代理路径【如果有】
    if arrs['proxy'] != '':
        proxy = arrs['proxy']
    for key in keys:
        tinify.key = key
        if (proxy != ''):
            tinify.proxy = proxy
        remain = tinify.compression_count
        if remain is None:
            remain_num_list[key] = 200
            remain_all_num += 200
        else:
            remain_num_list[key] = 200 - remain
            remain_all_num += 200 - remain
    # 判断当前的剩余值是否还够本次的压缩需求
    if len(img_list) > remain_all_num:
        print("the remain tiny pic num is ", remain_all_num, ',but your img is ', img_list.count,
              ',pls add a new key or change another key!!')
        sys.exit()
    tasks = alloc_tasks(remain_num_list, img_list, img_tar_list)
    # 开始处理任务列表
    for key in tasks:
        for num in range(len(tasks[key]['img'])):
            img = tasks[key]['img'][num]
            tar = tasks[key]['tar'][num]
            print("process the img:", img, " ...")
            tar_dir = os.path.dirname(tar)
            if not os.path.exists(tar_dir):
                os.mkdir(tar_dir)
            if not os.path.exists(img):
                print("the file:", img, " is not exists!!!")
                break
            tinify.key = key
            source = tinify.from_file(img)
            source.to_file(tar)
    print("process finished!!!")
