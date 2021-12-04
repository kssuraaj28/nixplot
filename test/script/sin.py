#!/usr/bin/env python3

def main():
    from time import sleep
    import numpy as np
    import sys
    inc = 0.01
    i = 0
    for _ in range(3000):
        sleep(0.01)
        print(i,np.sin(i))
        sys.stdout.flush()
        i+=inc


if __name__ == '__main__':
    main()
