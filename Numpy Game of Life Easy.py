# -*- coding: utf-8 -*-
"""Libraries Imported"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

"""Initial SEED for the System"""

Z=np.zeros((80,80)) #The Complete Map
Z[35:65,35:65]=np.random.randint(0,4,(30,30)) #The Random Seed

def neighbours(Z,n):
    N = np.zeros(Z.shape, int)
    #Add all surounding elements and divide by n
    N[1:-1,1:-1] += (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
                      Z[1:-1,0:-2]                + Z[1:-1,2:] +
                      Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])
    N=N/n
    return N



"""Function To Iterarte The Game of Life"""

def iterate(Z):
    
    #Z1 is the the initial state of system (Stored for further use)    
    Z1=np.empty_like(Z)
    Z1[:]=Z
    
    """Count neighbours of Type 3"""
    
    Z[:]=Z1
    Z_ = Z.ravel() #ravel opens up an array into a linear list
    
    """Selecting elements of type 1 and 2 and making them 0"""
    
    S1=np.argwhere((Z_==1)|(Z_==2))
    Z_[S1]=0
    
    """N3 is an array which consists the number of 3s surrounding 
       any element"""
    
                      
    N3=neighbours(Z,3)
    
    #Return Z to its original State
    Z[:]=Z1
    Z_ = Z.ravel()
    
    """Count neighbours of Type 1"""
    
    """Selecting elements of type 2 and 3 and making them 0"""
    
    S2=np.argwhere((Z_==2)|(Z_==3))
    Z_[S2]=0
    
    """N3 is an array which consists the number of 1s surrounding 
       any element"""    
    
    N1=neighbours(Z,1)
    
    #Return Z to its original State             
    Z[:]=Z1
    Z_ = Z.ravel()
    
    """Count neighbours of Type 2"""
    
    """Selecting elements of type 1 and 3 and making them 0"""    
    
    S3=np.argwhere((Z_==1)|(Z_==3))  
    Z_[S3]=0
    
    N2=neighbours(Z,2)
    
    """Count neighbours of Type 0"""    
    
    N0 = np.zeros(Z.shape, int)
    N0=8-N1+N2+N3
    
    
    #Return Z to its original State     
    Z[:]=Z1
    Z_=Z.ravel()
    
    #use ravel to open up arrays for better use
    N1_=N1.ravel()
    N2_=N2.ravel()
    N3_=N3.ravel()
    N0_=N0.ravel()
    
    
    
    """Apply rules"""
    
    R1 = np.argwhere((Z_==0) & (N1_ >1)) #These arrays consist of those 
    R2 = np.argwhere((Z_==1) & (N2_ >2)) #which satisfy specified rules
    R3 = np.argwhere((Z_==1) & (N3_ >2))
    R4 = np.argwhere((Z_==1) & (N2_ >3))
    R5 = np.argwhere((Z_==2) & ((N3_ >3)|(N1_<3)))
    R6 = np.argwhere((Z_==3) & ((N2_<3)))
    R7 = np.argwhere((Z_==1) & ((N2_ >1)))
    R8 = np.argwhere(((N3_ >2)&(N2_>1)))
    R9 = np.argwhere(((N2_ >2)&(N1_>1)))
    
    """As arrays from numpy stay linked we have to make 
       separate arrays which are not linked"""    
    
    C1=np.empty_like(R1)
    C1[:]=R1 
    C2=np.empty_like(R2)
    C2[:]=R2 
    C3=np.empty_like(R3)
    C3[:]=R3 
    C4=np.empty_like(R4)
    C4[:]=R4 
    C5=np.empty_like(R5)
    C5[:]=R5 
    C6=np.empty_like(R6)
    C6[:]=R6 
    C7=np.empty_like(R7)
    C7[:]=R7
    C8=np.empty_like(R8)
    C8[:]=R8
    C9=np.empty_like(R9)
    C9[:]=R9
    
    """Set new values (Implement the Rules)"""
    
    Z_[C1] = 1  
    Z_[C2] = 2
    Z_[C3] = 3
    Z_[C4] = 0
    Z_[C5] = 0   
    Z_[C6] = 1
    Z_[C7] = 0
    Z_[C8] = 3
    Z_[C9] = 2
    
    
    """Make sure borders stay null"""
    
    Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0




"""Making a Colourmap of Required Colours"""

cmap=colors.ListedColormap(['brown','green','blue','red'])

"""To Continuously Iterate our function"""

for gen in range(1000):
    iterate (Z)
    
    """Plotting"""    

    plt.imshow(Z,interpolation ='nearest',cmap=cmap)
    plt.show(block=False)
    plt.pause(0.000001)
    
    
    
    