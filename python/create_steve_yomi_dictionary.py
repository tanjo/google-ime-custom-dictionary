#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
create_steve_yomi_dictionary.py
    steve.txt の 'よみ' を 'すてぃーぶ' にした辞書を作成します
    これを作成することで 'すてぃーぶ' と入力するとsteve.txt に
    存在するレス画像一覧を入力することができます
"""
__author__ = "tanjo"
__version__ = "0.0.1"
__date__ = "2014-05-14"

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
        self._contents = self._line.split('\t') # => ['よみ', '単語', '品詞', 'コメント']
        if (len(self._contents) == 4):
            self._yomi = self._contents[0]
            self._tango = self._contents[1]
            self._hinshi = self._contents[2]
            self._comment = self._contents[3]

    def yomi_steve_line(self):
        """
        よみがすてぃーぶになっている単語の情報を返します
        """
        return 'すてぃーぶ' + '\t' + self._tango + '\t' + self._hinshi + '\t' + self._comment

def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 2):
        print('You must be following to use this.\n    ./create_steve_yomi_dictionary.py [file]')
        sys.exit(1)
    
    _filename = argvs[1]

    # file 読み込み
    _file = open(_filename)
    _yomi_steve_lines = []

    # 1行ずつ読み込む
    _line = _file.readline()
    while _line:
      _wordInfo = WordInfo(_line)
      _yomi_steve_lines.append(_wordInfo.yomi_steve_line())
      _line = _file.readline()
    _file.close()

    if (len(_yomi_steve_lines) == 0):
      sys.exit(1)

    # file 作成
    _splited_filename = _filename.rsplit('.', 1)
    if (len(_splited_filename) == 2):
        _save_filename = _splited_filename[0] + '_yomi_steve.' + _splited_filename[1]
    else:
        _save_filename = _filename + '_yomi_steve.txt'

    # 書き込み
    _file = open(_save_filename, 'w')
    _file.writelines(_yomi_steve_lines)
    _file.close()

    sys.exit(0)

if __name__ == '__main__':
    main()



