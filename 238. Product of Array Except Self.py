class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        arr = [0] * L
        zeros = []
        prod = 1

#Tracking zeros & product of the array excluding zeros
        
      for i in range(L):
            if nums[i] == 0:
                zeros.append(i)
            elif nums[i] != 0:
                prod = prod * nums[i]

#Checking all edge cases:

        if len(zeros) == 0:    #if no zeros then each element = product of array / value of the index
            for i in range(L):
                arr[i] = int(prod/nums[i])
            return arr
        
        elif len(zeros) > 1:  #if more than 1 zeros then product will always be zero
            return arr

        else:
            for i in range(L): #if one zero then except that element all else will be zero & that value will be product which we calculated excluding zeros
                if i in zeros:
                    arr[i] = prod
            return arr
            

            
