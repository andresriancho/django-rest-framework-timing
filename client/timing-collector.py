#!/usr/bin/env python

import sys
import requests


TOKEN = 'c346f10f02107ce7e12386be3abbb9032d19af20'
URL = 'http://127.0.0.1:8000/users/'
NUM_SAMPLES = 100000
OUTPUT = 'token-timing-%s.txt' % TOKEN


def progress(count, total, suffix=''):
    bar_len = 80
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben


def send_requests():
    session = requests.Session()
    output = file(OUTPUT, 'w')

    for i in xrange(NUM_SAMPLES):
        response = session.get(URL, headers={'Authorization': 'Token %s' % TOKEN})
        output.write('%s\n' % response.headers['X-Runtime'])

        if i % 500 == 0:
            progress(i, NUM_SAMPLES)

if __name__ == '__main__':
    send_requests()