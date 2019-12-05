import re
from parser import * 

def main():
    new_list = parse_inodes('/Users/Carlos/Projects/OS341/practical_3/fs2.txt')
    final_dbl = parse_datablocks('/Users/Carlos/Projects/OS341/practical_3/fs2.txt')
    block_traversal(final_dbl, new_list)

def block_traversal(final_dbl, new_list):
    print('Hello')


if __name__ == "__main__":
    main()