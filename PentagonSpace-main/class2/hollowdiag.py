for i in range(1,6,1):
    for j in range(1,6,1):
        if(i==5 or j == 1 or i==j):      
            print( "* ",end="") 
        elif(i==1 or j==5 ):
            print("+ ",end="")    
        else:
            print("  ",end="")    
    print("")       