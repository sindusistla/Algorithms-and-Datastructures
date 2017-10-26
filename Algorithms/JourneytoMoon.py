#Journey to moon

#Take input

def CheckInList(Countries_list,Country):
    CountryPresent=False;
    if (Country in Countries_list):
        # Country present in list
        CountryPresent=True;
    return CountryPresent

def CheckinGroupsList(Countries_list,Country):
    Group_num=0;


def GroupingofCountries(groups_lists,tuple_array):
    for i in range(0,len(tuple_array)):
        foundin_country_list=0
        for j in range(0,len(groups_lists)):
            if (CheckInList(groups_lists[j],tuple_array[i][0])== True and CheckInList(groups_lists[j],tuple_array[i][1])== True):
                # Combine both groups


            elif (CheckInList(groups_lists[j],tuple_array[i][0])== True and CheckInList(groups_lists[j],tuple_array[i][1])== False):
                if (CheckInList(groups_lists[j],tuple_array[i][1])==False ):
                    # if a_tuple is present add b_tuple to the list
                    groups_lists[j].append(tuple_array[i][1]);
                foundin_country_list=1;
            elif (CheckInList(groups_lists[j],tuple_array[i][1])== True and CheckInList(groups_lists[j],tuple_array[i][0])== False):
                if (CheckInList(groups_lists[j],tuple_array[i][0]) ==False):
                    # if b_tuple is found in the list add a element
                    groups_lists[j].append(tuple_array[i][0]);
                foundin_country_list=1;
        if (foundin_country_list == 0):
            temp_list=[];
            temp_list.append(tuple_array[i][0]);
            temp_list.append(tuple_array[i][1]);
            groups_lists.append(temp_list);

def CalculateSets(tuple_array, num_integers, groups_lists):
    NoOfExclusions=0;
    print(groups_lists)
    for i in range (0,len(groups_lists)):
        lenghtoflist=len(groups_lists[i]);
        if (lenghtoflist==2):
            # Only one combination is excluded
            NoOfExclusions=NoOfExclusions+1;
        elif (lenghtoflist >2):
            NoOfExclusions=NoOfExclusions+((lenghtoflist * (lenghtoflist-1))/2);

    TotalCombinations=(num_integers * (num_integers-1))/2
    Allowed_Combinations=TotalCombinations-NoOfExclusions;
    return Allowed_Combinations;

def main():
    num_sets=0;
    num_integers=0;
    Combinations=0;
    input_set=True;
    groups_lists=[];
    num_integers, num_sets = input().strip().split(' ');
    # Intializing the 10X2 matrix
    num_integers = int(num_integers);
    num_sets = int(num_sets);

    if ((num_integers >= 1 and num_integers <= pow(10,5) and (num_sets >=1 and num_sets <= pow(10,4)))):
        tuple_array = [[0 for i in range(2)] for j in range(num_sets)]
        for i in range(0, num_sets):
            a_tuple, b_tuple = input().strip().split(' ');
            a_tuple = int(a_tuple);
            b_tuple = int(b_tuple);
            if ((a_tuple < 0 or a_tuple > num_integers - 1) or (b_tuple < 0 or b_tuple > num_integers - 1)):
                input_set=False;
                break;
            tuple_array[i][0] = a_tuple;
            tuple_array[i][1] = b_tuple;
        if (input_set== True):
            GroupingofCountries(groups_lists, tuple_array)
            Combinations= CalculateSets(tuple_array, num_integers, groups_lists);
            Combinations=int(Combinations)
            print(Combinations)

main();
