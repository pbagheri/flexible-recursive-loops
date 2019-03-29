# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:49:30 2019

@author: Payam
"""

########################################## Functions:
# Flexible nested loops
def nest_loops(mins, maxs):
    r = 0
    inds = mins.copy()
    inds_df = pd.DataFrame()   
    while r >= 0: # while r (the rank in the inds array) is positive:
        while (r < (len(maxs) -1)): # while the rank at hand is lower than the last rank 
            if inds[r] < (maxs[r] + 1): # and if the last value in the rank at hand is not reached
                r += 1 # go to the next rank           
            else: # otherwise: 
                inds[r] = mins[r] # reset the value of inds (at the rank at hand) to the lowest value
                r -= 1 # go to the previous rank
                if r < 0: # if we fall lower than the lowest rank:             
                    break # breakout of the loops
                inds[r] += 1  # if not, add q to to inds at the new rank. Go to the inner while.          
        else: # when the inner while is not valid (i.e. r is the last rank):
            for i in range(mins[r], (maxs[r]+1)): # loop over the last rank
                inds[r] = i # put inds at the last rank equal to all possible values
                #print(inds)
                inds_df = inds_df.append(pd.Series(inds), ignore_index=True)
            r -= 1 # after the loop, go to the previous rank and
            inds[r] += 1 # add 1 to the value of d at that rank, go to the outer while
    return inds_df.astype(int)

