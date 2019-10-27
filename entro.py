import math
import itertools as it
from itertools import islice

def main():
    schedule_to_analyze = raw_input('please input the path to the schedule you want to analyze!\n')
    # count = 0
    un_process_list = []
    all_process_list = []

    with open(schedule_to_analyze) as f:
        for line in f:
            time_step, process_name = line.split()
            
            if process_name not in un_process_list:
                un_process_list.append(process_name)

            all_process_list.append(process_name)

        start = 0
        size = 100
        end = 0

        while start + size < len(all_process_list):
            start = end
            end = start + size
            chunk = list(it.islice(all_process_list, start, end))
        
            count_list = []

            for process in un_process_list:
                count_list.append(chunk.count(process))
            
            count_sum = float(sum(count_list))
            
            zipped = zip(un_process_list, count_list)
            
            entropy_list = []
            for process, count in zipped:
                value_to_entropy = count / count_sum
                entropy_list.append(entropy(value_to_entropy))
            print(abs(sum(entropy_list)))


def entropy(value):
    if value == 0:
        calc_value = 0
    else:
        logged_value = math.log(value, 2)
        # logged_value = math.log2(value) 
        calc_value = logged_value * value
    return calc_value

if __name__ == '__main__':
    main()