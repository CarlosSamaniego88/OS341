from pprint import pprint

def main():
    unique_page_counter('execution_large.txt')

def unique_page_counter(file_to_read):
    f = open(file_to_read,'r')
    f1 = f.readlines()
    page = ''
    page_list = []

    for line in f1:
        for bit in xrange(0,54):
            page += str(line[bit])
        page_list.append(page)
        page = ''

    change_count = 0
    current = page_list[0]
    for page in page_list:
        if current != page:
            change_count += 1
            current = page
        else:
            current = page
    print(change_count)
    
    print(page_list[:10])

    current = page_list[0]
    until_first_change_count = 0
    for page in page_list:
        if page == current:
            until_first_change_count += 1
        else:
            break

    print(until_first_change_count)

if __name__ == '__main__':
    main()