import re
from parser import * 

def main():
    #CHANGE THE PATHS AND THE "fs#.txt!!! all should match!"
    new_list = parse_inodes('/Users/Carlos/Projects/OS341/practical_3/fs2.txt')
    final_dbl = parse_datablocks('/Users/Carlos/Projects/OS341/practical_3/fs2.txt')
    access_file = '/Users/Carlos/Projects/OS341/practical_3/file_access2.txt'
    
    f = open(access_file,'r')
    lines = f.readlines()
    access_list = []
    
    for line in lines:
        line = line.replace('\n','')
        access_list.append(line)
    
    for thing in access_list:
        print('Block Traversal for file {}'.format(thing))
        filtered_thing = str(thing)
        filtered_thing = filtered_thing.replace('/','',1)
        filtered_thing = filtered_thing.split('/')
        inode = 0
        done = False
        i = 0

        while not done:
            dbl_index = re.findall(r'[-]?\d+?', new_list[inode])
            dbl_index = int(dbl_index[0])
            if dbl_index == -1:
                
                print('Inode : {}'.format(inode))
                print('Data : {}'.format(dbl_index))
                print('File {} : EMPTY'.format(thing))
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
                    print('File {}: {} '.format(thing,dbl))
                    done = True
                    break
            
            for item in dbl:
                try:
                    if filtered_thing[i] in item:
                        print('Inode : {}'.format(inode))
                        print('Data : {}'.format(dbl_index))
                        next_inode = re.findall(r'[-]?\d+?', item)
                        next_inode = int(next_inode[0])
                        next_start_data = re.findall(r'[-]?\d+?', new_list[next_inode])
                        next_start_data = int(next_start_data[0])
                        inode = next_inode
                except:
                    print('Inode : {}'.format(inode))
                    print('Data : {}'.format(dbl_index))
                    print('File {} : NOT FOUND'.format(thing))
                    done = True
                    break
            i+=1

if __name__ == "__main__":
    main()