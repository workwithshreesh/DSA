class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        count_number={}
        result=0
        for count in arr:
            if count not in count_number:
                count_number[count]=1
            else:
                count_number[count]+=1

        for key,value in count_number.items():
            if k!=0:
                if value==1:
                    arr.remove(key)
                    count_number.pop(key)
                    k-=1

        copy_count_number=count_number.copy()
        for key,value in copy_count_number.items():
            if value>1 and k!=0:
                arr.remove(key)
                count_number[key]=count_number[key]-1
                k-=1
            if value==0 or value==1:
                del count_number[key]
                k-=1
        print(count_number)
        return len(count_number)


SOL=Solution()
a=SOL.findLeastNumOfUniqueInts([2,1,1,3,3,3],3)
print(a)
