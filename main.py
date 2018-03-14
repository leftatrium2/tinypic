# -*- coding: utf-8 -*-

from parse_arg import parse_args
from read_config import read_config
from parse_dir import parse_dir
import tinify
import sys

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
    arrs = read_config(config_path)
    keys = arrs['key']
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
            remain_num_list[key] = remain
            remain_all_num += remain
    # 判断当前的剩余值是否还够本次的压缩需求
    if img_list.count > remain_all_num:
        print("the remain tiny pic num is ", remain_all_num, ',but your img is ', img_list.count,
              ',pls add a new key or change another key!!')
        sys.exit()
