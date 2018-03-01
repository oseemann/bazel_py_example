from ft.liba.mod1 import powerof2, powerof3
from ft.liba.sub.submod1 import add

import psycopg2
from colored import fg, bg, attr

def main():
    print('Hello World, from tool1!')
    print('powerof2(5)=%s%s%s' % (fg('green'), powerof2(5), attr('reset')))
    print('powerof3(5)=%s%s%s' % (fg('red'), powerof3(5), attr('reset')))
    print('add(5, 7)=%s%s%s' % (fg('blue'), add(5, 7), attr('reset')))
    cur = psycopg2.connect(dsn='').cursor()
    cur.execute('SELECT current_timestamp')
    print(cur.fetchall())

if __name__ == '__main__':
    main()
