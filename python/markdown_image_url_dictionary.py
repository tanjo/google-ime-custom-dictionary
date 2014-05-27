#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
markdown_image_url_dictionary.py
    markdown 形式に変換
"""

__author__ = "tanjo"
__version__ = "0.0.1"
__date__ = "2014-05-27"

import sys
import re

class MarkdownWordInfo(object):
    """
    マークダウン主力用単語の情報
    """
    def __init__(self, line):
        """
        単語読み込み
        """
        self._line = line
        self._contents = self._line.split('\t') # => ['よみ', '単語', '品詞', 'コメント']
        if (len(self._contents) == 4):
            self._yomi = self._contents[0]
            self._tango = self._contents[1]
            self._hinshi = self._contents[2]
            self._comment = self._contents[3]
            
    def markdown_line(self):
        """
        マークダウン形式の行を出力
        """
        
        self._markdown_tango = re.sub(r'(.*) (https?://.*)',r'![\1](\2)', self._tango)
        return self._yomi + '\t' + self._markdown_tango + '\t' + self._hinshi + '\t' + self._comment
        
def main():
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 2):
        print("You must be following to use this.\n    ex) ./markdown_url_dictionary.py [file]")
        sys.exit(1)
    
    _filename = argvs[1]
    
    # file 読み込み
    _file = open(_filename)
    _markdown_lines = []
    
    # 1行ずつ読み込む
    _line = _file.readline()
    while _line:
        _wordInfo = MarkdownWordInfo(_line)
        _markdown_lines.append(_wordInfo.markdown_line())
        _line = _file.readline()
    _file.close()
    
    if (len(_markdown_lines) == 0):
        sys.exit(1)
        
    # file 作成
    _no_directory_filename = _filename.rsplit('/', 1)
    _splited_filename = []
    if (len(_no_directory_filename) > 1):
      _splited_filename = _no_directory_filename[0].rsplit('.', 1)
    else:
      _splited_filename = _filename.rsplit('.', 1)

    if (len(_splited_filename) == 2):
        _save_filename = 'augmented_tango/' + _splited_filename[0] + '_markdown_tango' + '.' + _splited_filename[1]
    else:
        _save_filename = 'augmented_tango/' + _splited_filename[0] + '_markdown_tango' + '.txt'
        
    # 書き込み
    _file = open(_save_filename, 'w')
    _file.writelines(_markdown_lines)
    _file.close()
    
    sys.exit(0)
    
if __name__ == '__main__':
    main()