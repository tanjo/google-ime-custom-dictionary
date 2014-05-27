#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
create_manual_yomi_dictionary.py
    file の 'よみ' を 任意のよみにした辞書を作成します
    これを作成することで任意のよみと入力すると file に
    存在するレス画像一覧を入力することができます
"""

__author__ = "tanjo"
__version__ = "0.0.1"
__date__ = "2014-05-16"

import re
import sys

class WordInfo(object):
    """
    単語の情報
    """
    def __init__(self, line):
        """
        [Tab]で区切ります
        """
        self._line = line
        self._contents = self._line.split('\t') # =>  ['よみ', '単語', '品詞', 'コメント']
        if (len(self._contents) == 4):
            self._yomi = self._contents[0]
            self._tango = self._contents[1]
            self._hinshi = self._contents[2]
            self._comment = self._contents[3]

    def change_yomi_line(self, yomi):
        """
        よみが yomi になっている単語の情報を返します
        """
        return yomi + '\t' + self._tango + '\t' + self._hinshi + '\t' + self._comment

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 3):
        print("You must be following to use this.\n    ex) ./create_steve_yomi_dictionary.py [file] [yomi]")
        sys.exit(1)

    _filename = argvs[1]
    _yomi = argvs[2]


    # file 読み込み
    _file = open(_filename)
    _yomi_lines = []

    # 1行ずつ読み込む
    _line = _file.readline()
    while _line:
        _wordInfo = WordInfo(_line)
        _yomi_lines.append(_wordInfo.change_yomi_line(_yomi))
        _line = _file.readline()
    _file.close()

    if (len(_yomi_lines) == 0):
        sys.exit(1)
    
    # file 作成
    _no_directory_filename = re.sub('/', '_', _filename)
    _splited_filename = []
    if (len(_no_directory_filename) > 1):
        _splited_filename = _no_directory_filename.rsplit('.', 1)
    else:
        _splited_filename = _filename.rsplit('.', 1)

    if (len(_splited_filename) == 2):
        _save_filename = 'augmented_yomi/' + _splited_filename[0] + '_yomi_' + _yomi + '.' + _splited_filename[1]
    else:
        _save_filename = 'augmented_yomi/' + _splited_filename[0] + '_yomi_' + _yomi + '.txt'

    # 書き込み
    _file = open(_save_filename, 'w')
    _file.writelines(_yomi_lines)
    _file.close()

    sys.exit(0)

if __name__ == '__main__':
    main()

