# Take input of Number of sequences and number of queries
import math;

def validate_input(num_sequence,num_queries):
    valid=0
    if (int(num_sequence) >= 1 and int(num_queries) >= 1 and int(num_queries) <= int(math.pow(10,5)) and int(num_sequence) <= int(math.pow(10,5))):
        # Input valid
        valid=1;
    return valid;


def main():
    num_sequence,num_queries=input().split(' ');
    if (validate_input(num_sequence, num_queries)!=1):
        return;

    arr_input=[];
    elements=[];
    seq=0;
    seq_list=[[] for i in range(0,int(num_sequence))];
    lastanswer=0;
    seq_lastanswer=0;
    # take input of quieries
    for j in range(0,int(num_queries)):
        input_num=input();
        validate_array=input_num.split();
        arr_input.append(input_num);
        if (int(validate_array[0]) !=1 and int(validate_array[0]) !=2):
            return;
        if(int(validate_array[1]) < 0 or int(validate_array[1]) > int(math.pow(10,9)) or int(validate_array[2]) < 0 or int(validate_array[2]) > int(math.pow(10,9))):
            return;


    for i in range (0,int(num_queries)):
        # Parse through the queires and find out the sequence
        elements=arr_input[i].split();
        seq=0;
        seq_lastanswer=0
        lastanswer_element=[];
        if ((int(elements[1]) >=0 and int(elements[1]) <= int(math.pow(10,9))) and (int(elements[2]) >=0 and int(elements[2]) <= int(math.pow(10,9)))):
            if (int(elements[0])==1 and int(num_sequence)>0):
                #print(elements[0])
                seq = ((int(elements[1]) ^ lastanswer) % int(num_sequence))
                seq_list[seq].append(elements[2]);
            elif (int(elements[0])==2 and int(num_sequence)>0 ):
                seq=((int(elements[1]) ^ lastanswer) % int(num_sequence));
                seq_list[seq].append(elements[2]);
                if (len(seq_list[seq]) >0 ):
                    seq_lastanswer=int(elements[2]) % len(seq_list[seq]);
                    lastanswer_element=seq_list[seq];
                    if (len(lastanswer_element)>0):
                        lastanswer=int(lastanswer_element[seq_lastanswer]);
                        print(lastanswer);
            else :
                return

main()