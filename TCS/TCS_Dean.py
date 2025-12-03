# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 11:39:26 2025

@author: chase
"""
def TCS(current_temp, target_temp):
    
    """TCS takes a current temperature and a target temperature as inputs, 
    corrects the current temperature towards the target, prints how much it is
    correcting the temp by, and outputs the new corrected temp."""
    
    #compute how much to correct temp by as a signed difference scaled by 25%
    correction = 0.25 * (target_temp - current_temp)
    
    #apply correction
    adjusted_temp = current_temp + correction
    
    #print how much TCS is adjusting current temperature by
    #use an if statement to state if increasing or decreasing temp because its funny. 
    if current_temp < target_temp:
        print(f"TCS increasing interior temperature by {correction:.2f} degrees for cold space humans")
    else: print(f"TCS decreasing interior temperature by {abs(correction):.2f} degrees for sweaty space humans")
    
    return adjusted_temp
