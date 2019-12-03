import re

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
    # print(final_dbl)    
    
    # for item in final_dbl:
    #     for subitem in item:
    #         print(subitem[1:3])

    #[['(.,0)', '(..,0)', '(p,1)', '(r,2)', '(w,3)'], ['(.,2)', '(..,0)', '(z,4)', '(u,3)'], ['k'], ['n'], [''], [''], [''], [''], [''], [''], [''], ['']]
    output = []
    for item in final_dbl:
        print(item)
        if len(item) > 3:
            iterateDir(item, type_list)
        else:
            pass

    # print(output)

    #cleans commas
    # final_output = []
    # for item in output:
    #     if ',' in item:
    #         item = item.replace(',','')
    #     print(item)

def iterateDir(item, type_list):
    for subitem in item:
        for num in range(-10,16):
            if subitem[num] == type_list.index(num):
                iterateDir(item)
        print('/'+subitem[1:3])


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

#current:
# /.
# /..
# /p
# /r
# /w
# /.
# /..
# /z
# /u