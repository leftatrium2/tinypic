# -*- coding: utf-8 -*-
import argparse


def parse_args():
    dicts = {}
    parser = argparse.ArgumentParser(description='tinypic is a tools for tinypng.com')
    parser.add_argument('-c', '--conf', help='config file path', action='store',
                        default='tinypic.config')
    parser.add_argument('-d', '--directory', help='target pic path', action='store')
    parser.add_argument('-t', '--target', help='Compressing image file path', action='store')
    arg = parser.parse_args()
    dicts['conf'] = arg.conf
    dicts['dict'] = arg.directory
    dicts['target'] = arg.target
    return dicts
