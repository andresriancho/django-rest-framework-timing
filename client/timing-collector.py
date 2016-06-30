#!/usr/bin/env python

import requests
import time
import sys

from utils.progress import progress
from CodernityDB.database import Database
from CodernityDB.index import IndexConflict

VALID_TOKEN_START = '224a93060c0dd4fb931d05083b4cb7b6a'
VALID_TOKEN_GUESS = '8c27df8'

TOTAL_LENGTH = len(VALID_TOKEN_START) + len(VALID_TOKEN_GUESS)
MISSING_CHAR_LENGTH = len(VALID_TOKEN_GUESS)

PADDING_CHAR = '0'

URL = 'http://127.0.0.1:8000/users/'
NUM_SAMPLES = 10000
OUTPUT_DB = 'token-timing.db'

TEST_NAME = sys.argv[1]


def generate_test_token(known_valid, test_char, missing_chars):
    return (known_valid +
            test_char +
            PADDING_CHAR * (missing_chars - 1))


def send_with_naive_timing(session, url, token):
    start = time.time()
    response = session.get(url, headers={'Authorization': 'Token %s' % token})
    end = time.time()

    return response, end-start


def send_requests(db, known_valid, test_case_1, test_case_2, missing_chars):
    """
    :param db: The database where samples are stored
    :param known_valid: The known valid characters
    :param test_case_1: One character to test (test case 1)
    :param test_case_2: One character to test (test case 2)
    :param missing_chars: The total number of chars of the API key
    :return: None. All is stored in the DB
    """
    session = requests.Session()

    token_test_case_1 = generate_test_token(known_valid,
                                            test_case_1,
                                            missing_chars)

    token_test_case_2 = generate_test_token(known_valid,
                                            test_case_2,
                                            missing_chars)

    print('Running test cases:')
    print(' - %s' % token_test_case_1)
    print(' - %s' % token_test_case_2)
    print('')
    print('Test name: %s' % TEST_NAME)

    for i in xrange(NUM_SAMPLES):

        #
        # What I'm trying to do here is to get timings in pairs.
        # https://github.com/andresriancho/django-rest-framework-timing/issues/5
        #
        tmp_results = {}

        for j, token in enumerate((token_test_case_1, token_test_case_2)):
            response, naive_time = send_with_naive_timing(session, URL, token)
            tmp_results[j] = (response, naive_time, token)

        data = {'test_name': TEST_NAME,
                'capture_timestamp': time.time()}

        for j, (response, naive_time, token) in enumerate(tmp_results.values()):
            data.update({'x_runtime_%s' % j: response.headers['X-Runtime'],
                         'naive_time_%s' % j: naive_time,
                         'token_%s' % j: token})

        db.insert(data)

        if i % (NUM_SAMPLES / 1000) == 0:
            progress(i, NUM_SAMPLES)


def warm_up(token):
    """
    Use different TCP/IP connections to warm up all the threads
    """
    for i in xrange(20):
        requests.get(URL, headers={'Authorization': 'Token %s' % token})


def init_db():
    db = Database(OUTPUT_DB)

    try:
        db.create()
    except IndexConflict:
        db.open()

    return db


if __name__ == '__main__':
    FAIL_1 = '7'
    FAIL_2 = '0'
    FAIL_3 = '1'
    SUCCESS = '8'

    try:
        db = init_db()
        warm_up(generate_test_token(VALID_TOKEN_START, '0', MISSING_CHAR_LENGTH))
        send_requests(db, VALID_TOKEN_START, FAIL_1, FAIL_2, MISSING_CHAR_LENGTH)
    except KeyboardInterrupt:
        print('')
        print('User pressed Ctrl+C.')
