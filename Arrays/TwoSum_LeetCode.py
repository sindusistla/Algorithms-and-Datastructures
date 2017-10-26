class Solution:
    def findElement(self,nums,Value,first_element,last_element):
        mid_index=int(first_element+(last_element-first_element)/2)
        if(nums[mid_index]== Value):
            return mid_index
        elif(nums[mid_index]> Value):
            # then value lies in frist half
            self.findElement(nums,Value,first_element,mid_index-1)
        elif(nums[mid_index]< Value):
            # then value lies in Second half
            self.findElement(nums,Value,mid_index+1,last_element)
        elif(first_element>= last_element or last_element < first_element):
            return False;

    def twoSum(self, nums, target):
        # nums is list
        # target is int
        # return type is list

        return_list=[]
        for i in range(0,len(nums)-1):
            difference=target-nums[i];
            # Search if difference exists in the list
            second_Num=self.findElement(nums,difference,0,len(nums)-1)
            if(second_Num > 0):
                # value is found
                return_list.append(i);
                return_list.append(second_Num);
                return return_list
            else:
                return False
