def subsets(nums):
    res=[]
    current=[]
    def backtrack(i):
        if i==len(nums):
            res.append(current.copy())
            return
    