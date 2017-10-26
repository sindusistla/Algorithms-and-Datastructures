# Circular rotation of array 


arr1 = [ ];
input_string=input();
input_arr=input_string.split(" ");
# input array
s = input()
arr1 = list(map(int, s.split()))
for i in range(0,int(input_arr[1])):
   arr1.append(arr1[0]);
   arr1.remove(arr1[0]);

print (' '.join(str(x) for x in arr1));

