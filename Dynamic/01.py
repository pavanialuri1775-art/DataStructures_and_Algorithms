#leetcode 605 can place flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:# when there is no need to plant a flower
            return True
        for i in range(len(flowerbed)):#01234
            if flowerbed[i] == 0: #i=0
            #check left side
                l = (i == 0 or flowerbed[i - 1] == 0) 
                #check right side
                r = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0) #prev and next position 1,0,1,0,1

                if l and r: #compare left and right 
                    flowerbed[i] = 1 
                    n =n- 1 # 1-1=0, 2-1=0,1-1=0 after planting it will become empty and return true

                    if n == 0: #
                        return True

        return False # all checking is completed and no space to plant return false