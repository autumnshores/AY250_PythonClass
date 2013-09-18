# Calculate module

import argparse
parser = argparse.ArgumentParser(description='Calculate Stuff')
parser.add_argument('required_arg_1', help='This positional argument is required')
parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

results = parser.parse_args()
print 'required_args    =', results.required_string_1
print 'simple_value     =', results.simple_value


def Calculate(n):
    answer = eval(n)
    return answer

if __name__ == "__main__":
    import sys
    Calculate(str(sys.argv[1]))