# Program to find the sequence number using the two given quieries on the list of sequences


# take input

sequence_size,query_size=input().split(' ');
elements=[];
arr_input=[];
#arr_input=[[0 for x in range(0,int(query_size))] for y in range(0,3)]
# Take input of Sequence_size quries
for i in range (0,int(query_size)-1):
    # queries
    elements[i].append(input().split(' '));
    arr_input[i].append(elements);
    print( i)
print (arr_input)

# Input is in array arr_input
'''lastanswer=0
seq=0
new_seq = [[0 for x in range(sequence_size)] for y in range(sequence_size-1)] 


for i in range (0,query_size):
        seq=0;
        if (arr_input[i,0] == 1):
            # Perform query 1
            seq=((arr_input[i,1]^lastanswer)%sequence_size)
            new_seq.insert(seq,arr_input[i,2]);
        elif (arr_input[i,0]==2):
            #perform query 2
            seq=((arr_input[i,1]^lastanswer)%sequence_size)
            new_seq.insert(seq,arr_input[i,j])
            if (len(new_seq) > 0):
                lastanswer=y%len(new_seq);
                print(lastanswer)
        else:
            #Invalid input break
            break;'''