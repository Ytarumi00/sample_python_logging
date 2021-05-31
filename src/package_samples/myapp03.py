#!python3

"""ロガーの設定テスト

main関数でモジュール側のロガー設定を変更．
ルートロガーには変更を加えない方法かつ設定ファイル(logging_for_myapp03.conf)によって
設定を外だししたもの

 """


import os
import logging
import logging.config
import logging.handlers
import package3.fileconfig_logger

configfile_path = os.path.join(os.path.dirname(
    __file__), "logging_for_myapp03.conf")


def main():
    print(configfile_path)
    print('#--main start--#')
    logging.config.fileConfig(configfile_path)
    package3.fileconfig_logger.some_method1()

    print('#--main end--#')


if __name__ == '__main__':
    main()
