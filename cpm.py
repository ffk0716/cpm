#!/usr/bin/env python3
    
def count(**args):
    mr = args['rate'] / 100 / 12
    N = args['year'] * 12
    R = (1 + mr) ** N
    class temp: pass
    r = temp()
    r.cr = (R * mr) / (R - 1)
    r.c = round(r.cr * args['principal'])
    r.total = r.c * N
    r.total_int = r.total - args['principal']
    return r

def print2d(t):
    assert len(t) > 0
    t2 = [[str(e) for e in row] for row in t]
    lens = [max(len(i.encode('gbk')) for i in col) for col in zip(*t2)]
    table = []
    for row in t2:
        row2 = []
        for i in zip(lens, row):
            row2.append(' ' * (i[0] - len(i[1].encode('gbk'))) + i[1])
        table.append('  '.join(row2))
    print('\n'.join(table))

if __name__ == '__main__':
    import argparse
    
    mode = ['simple', 'all']
    
    parser = argparse.ArgumentParser(
            description='本息平均攤還法(Constant Payment Mortgage loan, CPM)，攤還金額試算',
            epilog="謹慎理財 信用至上")
    parser.add_argument('mode', choices = mode, nargs='?', default = mode[0], help='simple：簡單模式，all：印出每期攤還金額')
    parser.add_argument('-p', required = True, type=float, help='本金（萬元）(principal)')
    parser.add_argument('-r', required = True, type=float, help='年利率(annual percentage rate)')
    parser.add_argument('-y', required = True, type=int,   help='貸款年數(Years of Loan)')
    args = parser.parse_args()
    
    mr = args.r / 100 / 12
    P0 = round(args.p * 10000)
    N = args.y * 12
    c = count(year = args.y, rate = args.r, principal = P0).c
    
    def p(v):
        return '{:.1f}%'.format(v * 100)
    
    table = []
    table.append(['本金：', '{}萬元'.format(args.p)])
    table.append(['貸款年數：', '{}年'.format(args.y)])
    table.append(['年利率：', '{}%'.format(args.r)])
    table.append(['每月攤還金額：', '{}元'.format(c)])
    total_interest = c * N - P0
    table.append(['全部利息：', '{}元'.format(total_interest)])
    table.append(['利息本金比：', p(total_interest / P0)])
    print2d(table)
    
    rP = P0
    if args.mode == 'all':
        table = [['期數', '攤還本金', '攤還利息', '剩餘本金', '剩餘本金百分比']]
        for i in range(N):
            t = rP * mr 
            t = round(t)
            rP -= (c - t)
            table.append([i + 1, c - t, t, rP, p(rP / P0)])
        print2d(table)
