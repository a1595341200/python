'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-11-10 11:49:52
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-11-10 11:51:49
FilePath: /python/python/argparse/argparse.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import argparse
parser = argparse.ArgumentParser(description='计算两个数字的和')
parser.add_argument('num1', type=int, help='第一个数字')
parser.add_argument('num2', type=int, help='第二个数字')
parser.add_argument('--operator', type=str, choices=['+', '-', '*'], default='+', help='操作符')

args = parser.parse_args()
if args.operator == '+':
    result = args.num1 + args.num2
elif args.operator == '-':
    result = args.num1 - args.num2
elif args.operator == '*':
    result = args.num1 * args.num2
    
print('结果：', result)
