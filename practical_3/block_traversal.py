import re
from parser import * 

def main():
    new_list = parse_inodes('/Users/Carlos/Projects/OS341/practical_3/fs1.txt')
    final_dbl = parse_datablocks('/Users/Carlos/Projects/OS341/practical_3/fs1.txt')
    access_file = '/Users/Carlos/Projects/OS341/practical_3/file_access1.txt'
    
    f = open(access_file,'r')
    lines = f.readlines()
    access_list = []
    
    for line in lines:
        line = line.replace('\n','')
        access_list.append(line)
    
    # test = access_list[0]
    # test = str(test)
    # test = test.replace('/','',1)
    # test = test.split('/')
    # print(test)

    # test = access_list[0]
    # test = str(test)
    # test = test.replace('/','',1)
    # test = test.split('/')
    # print(test)

    ################################################## ATTEMPT 1 ##################################################
    # print('Block Traversal for file {}'.format(access_list[0]))
    # i = 0
    # start_data = 0
    # inode_index = final_dbl.index(final_dbl[0])
    # for item in final_dbl:
    #     for subitem in item:
    #         if subitem:
    #             if i < len(test):
    #                 if test[i] in subitem:
    #                     # print('test[i] is', test[i])
    #                     print('Inode : {}'.format(inode_index))
    #                     print('Data : {}'.format(start_data))
                        
    #                     next_index = re.findall(r'\d+', subitem)
    #                     next_index = str(next_index[0])
    #                     other_inode_index = new_list[int(next_index)]
                    
    #                     next_start_data = re.findall(r'\d+', other_inode_index)
    #                     next_start_data = next_start_data[0]
                        
    #                     start_data = next_start_data
    #                     inode_index = next_index
    #             print('Inode : {}'.format(next_index))
    #             print('Data : {}'.format(start_data))
    #                     #if data is -1:                         #pseudo
    #                         #print('File {} : EMPTY'.format(test)) 

    #     i+=1
    
    ################################################## ATTEMPT 2 ##################################################
    #works for 0,1,2,4,5
    #doessn't work for 3
    test = access_list[3]
    test = str(test)
    test = test.replace('/','',1)
    test = test.split('/')
    # ['/r/u', '/p', '/r/z', '/r/test', '/n', '/w']
    # ['d -> a:0', 'f -> a:2', 'd -> a:1', 'f -> a:-1', 'f -> a:3', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']
    # [['(.,0)', '(..,0)', '(p,1)', '(r,2)', '(w,3)'], ['(.,2)', '(..,0)', '(z,4)', '(u,3)'], ['k'], ['n'], [''], [''], [''], [''], [''], [''], [''], ['']]
    inode = 0
    done = False
    i = 0
    # print(final_dbl[inode])
    while not done:
        dbl_index = re.findall(r'[-]?\d+?', new_list[inode])
        dbl_index = int(dbl_index[0])
        # print('dbl_index is, {}'.format(dbl_index))
        if dbl_index == -1:
            print('Inode : {}'.format(inode))
            print('Data : {}'.format(dbl_index))
            print('File {} : EMPTY'.format(access_list[3]))
            done = True
            break
        else:
            dbl = final_dbl[dbl_index]
            if 'd' in new_list[inode]:
                dbl = final_dbl[dbl_index]
            
            elif 'f' in new_list[inode]:
                print('Inode : {}'.format(inode))
                print('Data : {}'.format(dbl_index))
                dbl = str(dbl[0])
                print('File {}: {} '.format(access_list[3],dbl))
                done = True
                break
            # else:
            #     print('Inode : {}'.format(inode))
            #     print('Data : {}'.format(dbl_index))
            #     print('File {} : NOT FOUND'.format(access_list[3]))
            #     done = True
        
        for item in dbl:
            if test[i] in item:
                print('Inode : {}'.format(inode))
                print('Data : {}'.format(dbl_index))
                next_inode = re.findall(r'[-]?\d+?', item)
                next_inode = int(next_inode[0])
                # print('next inode is, {}'.format(next_inode))
                next_start_data = re.findall(r'[-]?\d+?', new_list[next_inode])
                next_start_data = int(next_start_data[0])
                # print('next start data is, {}'.format(next_start_data))
                inode = next_inode
        
        # print('Inode : {}'.format(inode))
        # print('Data : {}'.format(dbl_index))
        # print('File {} : NOT FOUND'.format(access_list[3]))
        # done = True
        i+=1

if __name__ == "__main__":
    main()