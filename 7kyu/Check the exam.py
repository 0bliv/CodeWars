def check_exam(arr1,arr2):
    resp = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            resp+=4
        elif arr2[i] == "":
            resp+= 0
        else:
            resp+=-1
    
    if resp < 0:
        return 0
    else:
        return resp
            
  
