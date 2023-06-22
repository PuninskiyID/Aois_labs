from nanologic import *




if __name__ == '__main__':
    h4 = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1]]
    h3 = [[0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [1]]
    h2 = [[0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1]]
    h1 = [[0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1]]
    V = [[0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1]]
    operands = ['q4', 'q3', 'q2', 'q1', 'V']

    print('_' * 100)
    print('SDNF minimalizatsiya [h1]', minimize_PDNF(h1, operands))
    print('_' * 100)
    print('SDNF minimalizatsiya [h2]', minimize_PDNF(h2, operands))
    print('_' * 100)
    print('SDNF minimalizatsiya [h3]', minimize_PDNF(h3, operands))
    print('_' * 100)
    print('SDNF minimalizatsiya [h4]', minimize_PDNF(h4, operands))
    print('_' * 100)