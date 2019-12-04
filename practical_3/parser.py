import re

def main():
    fs_parser('/Users/Carlos/Projects/OS341/practical_3/fs2.txt')

def fs_parser(file):
    f = open(file,'r')
    lines = f.readlines()

    i = 1
    # for line in lines:
    inode_num = lines[0]
    inode_num = int(inode_num)

    data_block_num = lines[1]
    data_block_num = int(data_block_num)

    inode_bitmap = lines[2]
    inode_bitmap = int(inode_bitmap)
    
    inode_set = lines[3]
    inode_set = str(inode_set)
    
    data_bitmap = lines[4]
    data_bitmap = int(data_bitmap)
    
    data_block_set = lines[5]
    data_block_set = str(data_block_set)


    ################ PARSED INODE_SET ################
    inode_set = inode_set.replace('[', '')
    inode_set = inode_set.replace(']', ',')
    inode_set = inode_set.replace(' ', '')
    inode_set = inode_set.split(',')
     
    isDir = 'Directory'
    isFile = 'File'
    new_list = []
    type_list = []
    for item in inode_set:
        if 'd' in item:
            item = item[0] + ' -> ' + item[1:]
            new_list.append(item)
            type_list.append(isDir)
        elif 'f' in item:
            item = item[0] + ' -> ' + item[1:]
            new_list.append(item)
            type_list.append(isFile)
    
    for i in range(inode_num-len(new_list)):
        new_list.append('Empty')
        type_list.append('Unknown')

    # print(new_list)
    # print(type_list)

    ################ PARSED DATA BLOCK SET ################
    data_block_set = data_block_set.split('] ')
    new_dbl = []
    for item in data_block_set:
        item += ']'
        new_dbl.append(item)
    
    length_dbl = len(new_dbl)
    new_dbl[len(new_dbl)-1] = new_dbl[len(new_dbl)-1][:-1]
    # print(new_dbl)

    final_dbl = []
    for item in new_dbl:
        if '[' in item:
            item = item.replace('[','')
        if ']' in item:
            item = item.replace(']','')
        item = item.split(' ')
        final_dbl.append(item)
  
    print(final_dbl)
    print(new_list)
    print(type_list)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #[['(.,0)', '(..,0)', '(p,1)', '(r,2)', '(w,3)'], ['(.,2)', '(..,0)', '(z,4)', '(u,3)'], ['k'], ['n'], [''], [''], [''], [''], [''], [''], [''], ['']]
    # for item in final_dbl:
    output = []
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
                # print('check is', check)
                check_index = re.findall(r'\d+', check)
                check_index = int(check_index[0])
                if 'f' in check:
                    comma_location = re.search(",", item).start()
                    print(starting_folder + item[1:comma_location])
                if 'd' in check:
                    # print(item[1:3])
                    printdir(final_dbl[check_index], starting_folder + item[1:comma_location]+'/', new_list, final_dbl)
        i+=1


if __name__ == "__main__":
    main()