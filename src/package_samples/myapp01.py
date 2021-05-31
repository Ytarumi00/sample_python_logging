#!python3

'''ロガーの設定テストコード

main関数でロガーの設定を行い，
別モジュール(package1/mylib)のメソッド(do_something())を実行した際の挙動確認用

'''

import logging
from package1 import mylib


def main():
    print('fuga')
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
