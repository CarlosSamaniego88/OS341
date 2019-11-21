def main():
    fs_parser('/Users/Carlos/Projects/OS341/practical_3/fs1.txt')

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
    # print(data_block_set)
    data_block_set = data_block_set.split('] ')
    # print(data_block_set)
    new_dbl = []
    for item in data_block_set:
        item += ']'
        new_dbl.append(item)
    print(new_dbl)

    for item in new_dbl:
        # print(item)
        item = item.replace(' ', ', ')
        # for subitem in item:
        #     subitem = subitem.replace(' ', ', ')
        # print(item)
        print(item)
        


    # data_block_set = data_block_set.replace('[', '')
    # data_block_set = data_block_set.replace(']', ':')
    # data_block_set = data_block_set.replace(' ', '')
    # # print(data_block_set)
    # data_block_set = data_block_set.split(':')
    # # print(data_block_set)
    # # print(len(data_block_set))
    # data_block_set.pop()
    # # print(data_block_set)
    # data_block_set_length = len(data_block_set)
    # # print(data_block_set_length)
    # #Done parsing

    # for item in data_block_set:
    #     item = item.split(',')
    #     # print(item)
    #     for subitem in item:
    #         if '(' in subitem or ')' in subitem:
    #             subitem = subitem.replace('(','')
    #             subitem = subitem.replace(')','')
    #             print(subitem)
    #         # if ')' in subitem:
    #         #     subitem = subitem.replace(')','')
    #         #     print(subitem)


    # for item in data_block_set:
    #     print(item)

    # current_directory = '/.'
    # back_directory = '/..'

    # print(current_directory)
    # print(back_directory)

    # for item in new_list:
        
    
if __name__ == "__main__":
    main()


# /.
# /..
# /p
# /r/.
# /r/..
# /r/z
# /r/u
# /w