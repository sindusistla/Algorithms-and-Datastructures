# Left array rotation

def array_left_rotation(a, n, k):
    for i in range(0,k):
        temp=a[0];
        a.remove(a[0]);
        a.append(temp);



# No of elements in array and no of rotations
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print (' '.join(str(e)for e in a ))