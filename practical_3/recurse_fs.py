import re
from parser import * 

def main():
    new_list = parse_inodes('/Users/Carlos/Projects/OS341/practical_3/fs2.txt')
    final_dbl = parse_datablocks('/Users/Carlos/Projects/OS341/practical_3/fs2.txt')

    print(new_list)
    print(final_dbl)
    printdir(final_dbl[0], '/', new_list, final_dbl)
    

def printdir(directory, starting_folder, new_list, final_dbl):
    i = 0
    print(starting_folder+'.')
    print(starting_folder+'..')
    for item in directory:
        if i > 1:
            index = re.findall(r'\d+', item)
            if index:
                index = int(index[0])
                check = str(new_list[index])
                check_index = re.findall(r'\d+', check)
                check_index = int(check_index[0])
                if 'f' in check:
                    comma_location = re.search(",", item).start()
                    print(starting_folder + item[1:comma_location])
                if 'd' in check:
                    printdir(final_dbl[check_index], starting_folder + item[1:comma_location]+'/', new_list, final_dbl)
        i+=1

if __name__ == "__main__":
    main()