
num_size,num_rows=input().strip().split(' ');
arr_output=[0]*int(num_size);

if (int(num_size) >=3 and int(num_size) <= pow(10,7)):
    for i in range (0,int(num_rows)):
        arr_input=list(map(int, input().strip().split(' ')));
        if ((int(arr_input[0]) <= int(arr_input[1])and (int(arr_input[0])<= int(num_size)) and int(arr_input[0]) <=int(num_size)) and int(arr_input[2]) <= pow(10,9)):
            for k in range(int(arr_input[0]),int(arr_input[1])):
                arr_output.insert(k,arr_output[k]+ arr_input[2]);
            if (int(arr_input[0])== int(arr_input[1])):
                arr_output.insert(int(arr_input[0]), arr_output[0] + arr_input[2])



print(max(arr_output));
