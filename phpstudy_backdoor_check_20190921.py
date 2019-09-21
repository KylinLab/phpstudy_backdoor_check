#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 10:17:13
# @Author  : cnmiaosi (cnmiaosi@qq.com)
# @Link    : https://www.cnmiaosi.cn/
# @Version : 1.0

import os
import sys
import string
import re

def check_file(filename):
    # 后门特征
    backdoor='@eval'
    # 行数 与 结果
    n = 0
    ckres = False
    # 暂只检测dll文件
    if filename.endswith('.dll'):
        with open(filename, "r", encoding='utf-8', errors='ignore') as rfp:
            for line in rfp:
                if backdoor in line:
                    ckres = True
                    break
                n += 1
    return ckres, n


def check_dir(ck_dir):
    # 检查目录
    for root, dirs, filenames in os.walk(ck_dir):
        for filename in filenames:
            ck_file = os.path.join(root, filename)
            check_res, text_line = check_file(ck_file)
            if check_res:
                print("backdoor ==>>> {0}, text_line: {1}".format(ck_file, text_line))
    pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("使用方法：{0} [phpstudy安装目录]".format(sys.argv[0]))
        sys.exit(1)
    check_dir(sys.argv[1])
