def sort(num, type):
    x = 0
    y = 0
    while num>0:
        if type == 0:
            x = y+2  #(num>0,0)  结果：x=2
            break
        elif type == 1:  #(num>0,1)  结果：x=10
            x = y+10
            break
        else:
            x = y+20    #x=20
            break
    return x
