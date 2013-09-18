# Calculate module

import argparse

def Calculate(n):
    answer = eval(n)
    return answer

if __name__ == "__main__":
    import sys
    Calculate(str(sys.argv[1]))