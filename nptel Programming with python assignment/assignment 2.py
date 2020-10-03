def three(m):
    for  i  in range(0,m):
        for j in range(0,m):
            for k in range(0,m):
                if(i*i + j*j + k*k == m):
                    return True
                elif(i >= m/2 and j>= m/2 and k>= m/2):
                    return False

                    
                    
                

    
