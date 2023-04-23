#!/usr/bin/env python

'''\
Browse bash.org from the comfort of your shell.\
'''

from __future__ import print_function, unicode_literals
from bs4 import BeautifulSoup
from sys import argv
from argparse import ArgumentParser
from random import sample
import requests


def get_quotes(option='r', num_quotes=1, vote_range=None, quote_id=None):
    base_url = 'http://bash.org/?'
    options_map = {'r': 'random1',
                   't': 'top2',
                   'l': 'latest'}

    if quote_id:
        url = base_url + quote_id
    else:
        url = base_url + options_map.get(option[0].lower(), 'random1')

    page = BeautifulSoup(requests.get(url).text, features="html5lib")

    quote_info = page.find_all('p', attrs={'class': 'quote'})
    quotes = page.find_all('p', attrs={'class': 'qt'})

    if vote_range:
        min_votes, max_votes = vote_range
        filtered_quotes = []
        filtered_info = []
        for info, quote in zip(quote_info, quotes):
            votes = int(info.find('font').get_text().strip('()'))
            if min_votes <= votes <= max_votes:
                filtered_info.append(info)
                filtered_quotes.append(quote)
        quote_info, quotes = filtered_info, filtered_quotes

    return quote_info, quotes


def print_quotes(option='r', num_quotes=1, vote_range=None, quote_id=None):
    quote_info, quotes = get_quotes(option, num_quotes, vote_range, quote_id)
    if quote_id:
        if quote_info and quotes:
            print('{0}\n{1}'.format(quote_info[0].get_text()[:-5], quotes[0].get_text()), end='\n\n')
        else:
            print("Quote not found.")
    else:
        num_quotes_to_return = min(abs(num_quotes), 50)
        for quote_num in sample(range(len(quotes)), num_quotes_to_return):
            info = quote_info[quote_num]
            quote = quotes[quote_num]
            print('{0}\n{1}'.format(info.get_text()[:-5], quote.get_text()), end='\n\n')


def main():
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

    r_help = 'Filter quotes by vote range (min,max).'
    parser.add_argument('-r',
                        '--range',
                        nargs=2,
                        help=r_help,
                        default=None,
                        dest='vote_range',
                        type=int,
                        metavar=('MIN', 'MAX'))

    parser.add_argument('quote_id',
                        nargs='?',
                        help='Retrieve a single quote by its ID.',
                        default=None,
                        type=str)

    args = parser.parse_args(argv[1:])
    print_quotes(args.option, args.num_quotes, args.vote_range, args.quote_id)


if __name__ == '__main__':
    main()
