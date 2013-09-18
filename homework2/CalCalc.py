# Calculate module

import argparse
parser = argparse.ArgumentParser(description='Calculate Stuff')
parser.add_argument('-s', action='store', dest='string',
                    help='Store a string (equation to calculate)')

results = parser.parse_args()


def Calculate(n):
    try:
        answer = eval(n)
        print answer
    except:
        print 'Cannot evaluate using eval(). Getting Wolfram Alpha to help...'
        import urllib2

if __name__ == "__main__":
    import sys
    Calculate(str(sys.argv[2]))