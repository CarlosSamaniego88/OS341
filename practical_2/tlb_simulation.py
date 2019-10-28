def main():
    size_of_tlb = input('Input size of TLB\n')
    tlb(size_of_tlb, 'execution_large.txt')

def tlb(size, file):
    f = open(file, 'r')
    f1 = f.readlines()
    page = ''
    page_list = []

    for line in f1:
        for bit in xrange(0,54):
            page += str(line[bit])
        page_list.append(page)
        page = ''
    
#    print(len(page_list))
    
    tlb_dict = {}
#    min_page = min(tlb_dict, key = tlb_dict.get)
    for page in page_list:
        if len(tlb_dict) < size:
            if page not in tlb_dict:
                tlb_dict[page] = 1
            elif page in tlb_dict:
                tlb_dict[page] += 1
        if len(tlb_dict) == size:
            min(tlb_dict, key = tlb_dict.get) = page
            break

    print(tlb_dict)


if __name__ == '__main__':
    main()

