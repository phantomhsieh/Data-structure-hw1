import argparse
import time
from struct import node, stack, queue

def main(struct, input_file, output_file):
    if struct == 'queue':
        test = queue()
    else:
        test = stack()

    input = open(input_file)
    output = open(output_file, 'w')

    # TODO: your should parse the input commands here
    

if __name__ == '__main__':
    # Do Not Change the code here
    parser = argparse.ArgumentParser()
    parser.add_argument('--structure', choices=['queue', 'stack'], default='stack')
    parser.add_argument('--input', default='./input.txt')
    parser.add_argument('--output', default='./output.txt')
    args = parser.parse_args()
    ts = time.time()
    main(args.structure, args.input, args.output)
    te = time.time()
    print('Ruun Time: {:.5f}s'.format(te-ts))
