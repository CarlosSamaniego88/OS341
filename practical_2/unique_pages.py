from pprint import pprint

def main():
    unique_page_counter('execution_large.txt')

def unique_page_counter(file_to_read):
    f = open(file_to_read,'r')
    f1 = f.readlines()
    page = ''
    offset = ''
    page_list = []
    offset_list = []

    for line in f1:
        for bit in xrange(0,54):
            page += str(line[bit])
        page_list.append(page)
        page = ''
    
        for bit in xrange(54,65):
            offset += str(line[bit])
        offset = offset.replace('\r','')
        offset_list.append(offset)
        offset = ''

    print(page_list)
    print(len(page_list))
    
    unique_page_list = {}
    for page in page_list:
        if page not in unique_page_list:
            unique_page_list[page] = 1
        else:
            unique_page_list[page] += 1
    pprint(unique_page_list)

if __name__ == '__main__':
    main()
