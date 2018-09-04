# coding:utf-8
import unittest
import os
import argparse
from lib import HTMLTestRunner
import cases
import reports
from commons.base_function import today_seconds


def create_suite(dir_name, pattern):
    """
    :param pattern:test_case下.py文件名称的格式
    :param dir_name: test_case文件夹的路径
    :return:返回装填后的测试套件
    """
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(dir_name, pattern=pattern+"*.py", top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
    return test_unit


def run(pattern):
    # 测试用例的路径
    dir_path = os.path.dirname(cases.__file__)
    # 获取装填后的测试套件
    all_tests = create_suite(dir_path, pattern)
    # 存放测试报告的路径
    filename = os.path.join(os.path.dirname(reports.__file__), today_seconds() + ".html")
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='API_Test_Report', description="tests_requirements")
    runner.run(all_tests)
    fp.close()


def main():
    parser = argparse.ArgumentParser(prog='command argument')
    parser.add_argument('-p', action='store', default="*", help='Get the test case starting with this pattern')
    options = parser.parse_args()
    pattern = options.p
    run(pattern)


if __name__ == "__main__":
    main()
