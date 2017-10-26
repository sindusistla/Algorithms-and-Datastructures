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
        if (arr_input[j]==arr_queries[i]):
            count=count+1;
    print (count)