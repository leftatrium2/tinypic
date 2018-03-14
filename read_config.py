# -*- coding: utf-8 -*-
import configparser
import os.path


def read_config(config_path):
    arrs = {'key': [], 'proxy': ''}
    if config_path is None:
        print("error in config path,is None")
        return
    if not os.path.exists(config_path):
        print("error in config path,is not exists")
        return
    cf = configparser.ConfigParser()
    cf.read(config_path)
    sections = cf.sections()
    if 'key' in sections:
        keys = cf.options('key')
        for key in keys:
            if key != '':
                arrs['key'].append(cf.get('key', key))
    if 'proxy' in sections:
        proxy_list = cf.options('proxy')
        for key in proxy_list:
            if key != '':
                arrs['proxy'] = cf.get('proxy', key)
    return arrs
