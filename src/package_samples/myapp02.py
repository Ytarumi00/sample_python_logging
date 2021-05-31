#!python3
"""ロガーの設定テストコード

main関数でモジュール側のロガー設定を変更．
ルートロガーには変更を加えない方法


"""


import logging
from package2 import mylib


def main():
    print("#--main start--#")

    # main側のロガー設定
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s -%(levelname)s - %(message)s"))
    handler.setLevel(logging.DEBUG)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    # モジュール側のロガー未設定で実施．モジュール側のログハンドラーがNullHandlerのため表示なし
    logger.info('Start non logging setting')
    mylib.do_something()
    logger.info('End non logging setting')
    print()

    # モジュール側のロガー設定をmainで実施
    logging.getLogger('package2').setLevel(logging.INFO)
    logging.getLogger('package2').addHandler(handler)

    logger.info('Start with logging setting')
    mylib.do_something()
    logger.info('End with logging setting')
    print()

    # モジュール側のロガー設定をDEBUGに変更
    logging.getLogger('package2').setLevel(logging.DEBUG)
    logging.getLogger('package2').addHandler(handler)

    logger.info('Start with logging setting')
    mylib.do_something()
    logger.info('End with logging setting')
    print()

    print("#--main end--#")


if __name__ == '__main__':
    main()
