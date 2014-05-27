#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
count_words_in_all_dictionaries.py
  ディレクトリにある .txt の行数を
  まとめて .html として書き出す
"""

__author__ = "tanjo"
__version__ = "0.0.1"
__date__ = "2014-05-27"

import sys
import os
import os.path

class CustomDictionary(object):
    """
    カスタム辞書
    """
    def __init__(self, dictionary_name):
        """
        辞書読み込み
        """
        self._dictionary_name = dictionary_name
    def number_of_words(self):
        """
        単語の数を数えます
        """
        d = open(self._dictionary_name);
        return sum(1 for line in d)

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc == 1):
        dirname = '.'
    elif (argc == 2):
        dirmane = argvs[2]
    files = []
    for name in os.listdir(dirname):
        if (os.path.isfile(name)):
            splitedname = name.split('.')
            if (len(splitedname) == 2):
                if (splitedname[1] == 'txt'):
                    files.append(name)
    print len(files)
    for f in files:
        dic = CustomDictionary(f)
        print f + " : " + str(dic.number_of_words())

if __name__ == '__main__':
    main()
