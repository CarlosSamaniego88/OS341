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
    tlb_miss = 0
    for page in page_list:
        if len(tlb_dict) < size:
            if page not in tlb_dict:
                tlb_dict[page] = 1
                tlb_miss += 1
            elif page in tlb_dict:
                tlb_dict[page] += 1
        elif len(tlb_dict) == size:
            min_page_key = min(tlb_dict, key = tlb_dict.get)
            del tlb_dict[min_page_key]
            if page not in tlb_dict:
                tlb_dict[page] = 1
                tlb_miss += 1
            elif page in tlb_dict:
                tlb_dict[page] += 1
        else:
            pass

    print(tlb_miss)

            # min_page_value = tlb_dict[min_page_key]
            # del tlb_dict[min_page_key]
            # tlb_dict[page] += 1
            # min_page_key, min_page_value = page.key, page.value
            # tlb_dict.update(min_page, min_dict_page, tlb_dict[page] = 1)
            # min_page = min(tlb_dict.keys())
            # print(min(tlb_dict, item = tlb_dict.get))
            # min_page = page
            # break
    # tlb_dict.
    # print(tlb_dict)
    # print(min(tlb_dict, key = tlb_dict.get))
    # min_page = min(tlb_dict, key = tlb_dict.get)
    # print(tlb_dict[min_page])
if __name__ == '__main__':
    main()

