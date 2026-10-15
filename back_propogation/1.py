def generate(n):
    str=[""]
    for i in range(n):
        new_str=[]
        for  j  in str:
            new_str.append(j+"A")
            new_str.append(j+'B')
        str=new_str
    print(str)
generate(2)
        
    
    
    
    