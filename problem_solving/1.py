##ls = [sun, mon, tue, wed, thur, fri, sat]
#mon, 2
#output= wed

#frid, 2000
#output: tue

days=["sun","mon","tue","wed","thur","fri","sat"]
day=input()
n=int(input())

indx=days.index(day)

new_index=(indx+n)%7
print(days[new_index])