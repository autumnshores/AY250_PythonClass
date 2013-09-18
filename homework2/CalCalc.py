#Calculate module

import argparse
parser = argparse.ArgumentParser(description='Calculate stuff')
parser.add_argument('-s', action='store', dest='string',
                    help='Store a string (equation to calculate)')

results = parser.parse_args()

def Calculate(n):
    try:
        answer = eval(n)
        print answer
    except:
        print 'Cannot calculate '+str(n)+' using eval(). Getting Wolfram Alpha to help...'
        import urllib2
        import urllib
        response = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input='+str(n.replace(' ','+')+'&appid=UAGAWR-3X6Y8W777Q'))
        print response.read() #Q2a not complete yet

def test_1():
    assert abs(4. - Calculate('2**2')) < .001

def test_2():

def test_3():

def test_4():

def test_5():

if __name__ == "__main__":
    import sys
    Calculate(str(sys.argv[2]))