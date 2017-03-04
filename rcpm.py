#!/usr/bin/env python3
import argparse

mode = ['simple', 'all']

parser = argparse.ArgumentParser(
        description='本息平均攤還法 (Constant Payment Mortgage loan, CPM)',
        epilog="謹慎理財 信用至上")
parser.add_argument('mode', choices = mode, nargs='?', default = mode[0], help='模式：an integer for the accumulator')
parser.add_argument('-p', required = True, type=float, help='本金（萬元）(principal)')
parser.add_argument('-i', required = True, type=float, help='總利息（萬元）(toal interest)')
parser.add_argument('-y', required = True, type=int,   help='貸款年數(Years of Loan)')
args = parser.parse_args()

P0 = round(args.p * 10000)
N = args.y * 12

def get_ti(mr):
    R = (1 + mr) ** N
    c = (R * mr) / (R - 1) * P0
    return c * N - P0

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

ti = args.i * 10000
for r in frange(0.001, 100, 0.0001):
    mr = r / 100 / 12
    ti2 = get_ti(mr)
    if ti2 > ti:
        print('年利率約為{:.3f}%'.format(r))
        break 
