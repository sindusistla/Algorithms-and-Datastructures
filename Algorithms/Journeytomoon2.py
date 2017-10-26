#Journey to moon

#Take input
def calculate_sets(tuple_array, num_sets, num_integers):
    groups_lists=[];
    # calculate total number of combinations
    total_combinations=(num_integers * num_integers-1)/2;
    # Grouping the combinations
    for i in range(0,len(tuple_array)):
        temp_list=[];
        temp_list.append(tuple_array[i][0])
        temp_list.append(tuple_array[i][1])
        # Traverse through the array
        for j in range(i+1,len(tuple_array)):
            # Check if the elements in the temp list
            if(temp_list.index(tuple_array[j][0]) > 0 ):
                # then add the other element of the set to the list
                temp_list.append(tuple_array[j][1]);
            elif (temp_list.index(tuple_array[j][1]) > 0):
                temp_list.append(tuple_array[j][0]);
            #else:
                #The tuple is not related to the astronaut country.
        groups_lists.append(temp_list);
    print(groups_lists);

def checkInGroups(groups_lists,tuple_array):
    for i in range(0,len(tuple_array)):
        foundin_group_list=0;
        temp_list=[];
        for j in range(0,len(groups_lists)):
           # print(groups_lists[j],tuple_array[i][0])
            try:
                if (groups_lists[j].index(tuple_array[i][0]) > 0  ):
                    # a_tuple exists
                    b_exists=0;
                    try:
                        if (groups_lists[j].index(tuple_array[i][1])>0):
                            # b_tuple already present in the list do not add again
                            raise ValueError("Already in list")
                            print("here")
                            b_exists=1;
                        # then add the other element of the set to the list
                    except ValueError:
                        if (ValueError == "Already in list" and b_exists !=1):
                            # but b_tuple does not exists only then add b_tuple
                            groups_lists[j].append(tuple_array[i][1]);
                    foundin_group_list=1;
                print(ValueError)
            except ValueError:
               # if (ValueError.find("is not in list") !=-1 ):
                    # the element does not exists add that elemnet to the list
                   # groups_lists[j].append(tuple_array[i][1]);
                #Do nothing
                foundin_group_list=0
            try:
                if (groups_lists[j].index(tuple_array[i][1]) > 0 and groups_lists[j].index(tuple_array[i][0])==0):
                    groups_lists[j].append(tuple_array[i][0]);
                    foundin_group_list=1;
            except ValueError:
                # Do nothing
                foundin_group_list=0;
        if (foundin_group_list==0):
            temp_list.append(tuple_array[i][0]);
            temp_list.append(tuple_array[i][1]);
            groups_lists.append(temp_list);

    print(groups_lists)

def main():
    num_sets=0;
    num_integers=0;
    groups_lists=[];
    num_integers, num_sets = input().strip().split(' ');
    # Intializing the 10X2 matrix
    num_integers = int(num_integers);
    num_sets = int(num_sets);
    tuple_array = [[0 for i in range(2)] for j in range(num_sets)]
    for i in range(0, num_sets):
        a_tuple, b_tuple = input().strip().split(' ');
        a_tuple = int(a_tuple);
        b_tuple = int(b_tuple);
        if ((a_tuple < 0 or a_tuple > num_integers - 1) or (b_tuple < 0 or b_tuple > num_integers - 1)):
            break;
        tuple_array[i][0] = a_tuple;
        tuple_array[i][1] = b_tuple;
        # take into an array
    #print(num_integers, num_sets)
   # print(tuple_array)

    #---------------------------------------------------------
    #calculate_sets(tuple_array, num_sets, num_integers)
    checkInGroups(groups_lists,tuple_array)
main();
