def main():
    size_of_tlb = input('Input size of TLB\n')
    tlb(size_of_tlb, 'execution_large.txt')

def tlb(size, file):
    f = open(file, 'r')
    f1 = f.readlines()
    page = ''
    page_list = []

    #reads in pages from file
    for line in f1:
        for bit in xrange(0,54):
            page += str(line[bit])
        page_list.append(page)
        page = ''
    
    #puts into dictionary and will replace key value pair with lowest value/count with new one.
    tlb_dict = {}
    tlb_miss = 0
    
    for page in page_list:
        if len(tlb_dict) < size:
            if page not in tlb_dict:
                tlb_dict[page] = 1
                tlb_miss += 1
            elif page in tlb_dict:
                tlb_dict[page] += 1
        elif len(tlb_dict) == size:
            if page not in tlb_dict:
                min_page_key = min(tlb_dict, key = tlb_dict.get)
                del tlb_dict[min_page_key]
                tlb_dict[page] = 1
                tlb_miss += 1
            elif page in tlb_dict:
                tlb_dict[page] += 1

    print('\n')
    print('Amount of TLB Misses: {}'.format(tlb_miss))

if __name__ == '__main__':
    main()

