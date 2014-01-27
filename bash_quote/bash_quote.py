#!/usr/bin/env python

'''\
Browse bash.org from the comfort fo your shell.\
'''


from __future__ import print_function, unicode_literals
from bs4 import BeautifulSoup
from sys import argv
from argparse import ArgumentParser
import requests



def get_quotes(option='r', num_quotes=1):
    '''\
    Get a list of quotes from bash.org.
    option -  which type of quotes you would like, (t)op, (l)atest or (r)andom
    num_quotes - number of quotes that you want printed, integer\
    '''
    base_url = 'http://bash.org/?'
    options_map = {'r': 'random1',
                   't': 'top2',
                   'l': 'latest'}

    if not option:
        option = 'r'

    url = base_url + options_map.get(option[0].lower(), 'random1')
    page = BeautifulSoup(requests.get(url).text)

    quote_info = page.find_all('p',
                               attrs={'class': 'quote'},
                               limit=num_quotes)
    quotes = page.find_all('p',
                           attrs={'class': 'qt'},
                           limit=num_quotes)

    return quote_info, quotes


def print_quotes(option='r', num_quotes=1):
    '''\
    Print quotes from bash.org.
    option -  which type of quotes you would like, (t)op, (l)atest or (r)andom
    num_quotes - number of quotes that you want printed, integer\
    '''
    quote_info, quotes = get_quotes(option, num_quotes)
    for info, quote in zip(quote_info, quotes):
        print('{0}\n{1}'.format(info.get_text()[:-5], quote.get_text()),
              end='\n\n')


def main():
    '''\
    Parse command line options and run get_quotes with options specified by the
    user\
    '''
    parser = ArgumentParser()
    n_help = 'Number of quotes you want returned'
    parser.add_argument('-n',
                        nargs='?',
                        help=n_help,
                        default=1,
                        dest='num_quotes',
                        type=int)

    opt_help = 'Which types of quotes you want returned.'
    parser.add_argument('-t',
                        '--type',
                        nargs='?',
                        help=opt_help,
                        default='r',
                        dest='option',
                        choices=('random', 'r', 'top', 't', 'latest', 'l'))

    args = parser.parse_args(argv[1:])
    print_quotes(args.option, args.num_quotes)


if __name__ == '__main__':
    main()
