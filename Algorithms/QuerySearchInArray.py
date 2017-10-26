# program to find the strings in given n strings
# give input

#Recursive find function
def find_recursive(start,end,SearchString,ArrayString):
    #search for item in string
   # print(SearchString,ArrayString,start,end);
    return ArrayString.find(SearchString,start,end)


#Input number of lines of input
input_size=input();
arr_input=[];
arr_queries=[];
for i in range (0,int(input_size)):
    arr_element=input();
    arr_input.append(arr_element);
#print(arr_input)
query_size=input();

for i in range(0,int(query_size)):
    query_elemnt=input();
    arr_queries.append(query_elemnt);
#print(arr_queries)
    # Processing Starts here
for i in range(0,int(query_size)):
    # Consider query
    #print('In i loop')
    count = 0;
    for j in range(0,int(input_size)):
        # Consider Array items
        start=0;
        #print('In j loop')
        end=len(arr_input[j])
        while True:
            find_return=find_recursive(start,end,arr_queries[i],arr_input[j]);
            #print(find_return)
            if (find_return >=0):
                #string found update start position of search and increase the count
                count=count+1;
                start=find_return+len(arr_queries[i]);
            else :
                # doesnt find the string break the loop
                break;
    print (count)