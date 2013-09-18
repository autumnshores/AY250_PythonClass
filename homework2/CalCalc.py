# Calculate module

import urllib2
import argparse
parser = argparse.ArgumentParser(description='Calculate Stuff')
parser.add_argument('-s', action='store', dest='string',
                    help='Store a string (equation to calculate)')

results = parser.parse_args()


def Calculate(n):
    answer = eval(n)
    print answer

if __name__ == "__main__":
    import sys
    Calculate(str(sys.argv[2]))