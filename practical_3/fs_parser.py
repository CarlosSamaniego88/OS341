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

    print(new_list)
    print(type_list)

if __name__ == "__main__":
    main()