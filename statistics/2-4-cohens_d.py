#!/usr/bin/env python
# -*- coding: utf-8 -*-



import math  ## for math functions like square-root (sqrt)
import nsfg  ## for reading and cleaning up data



# Exercise 2.4 Using the variable totalwgt_lb , investigate whether first ba-
# bies are lighter or heavier than others. Compute Cohen’s d to quantify the
# difference between the groups. How does it compare to the difference in
# pregnancy length?


## The nsfg.ReadFemPreg function performs a lot of data clean-up 
## that I don't want to re-type
preg = nsfg.ReadFemPreg()


live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]


"""
Check stats for 2 groups
"""
print 'Total weight stats:'

print 'Firsts mean', firsts.totalwgt_lb.mean()
## 7.201094430437772
print 'Others mean',others.totalwgt_lb.mean()
## 7.325855614973262

# First babies are generally lower weight than later babies, but not by much.

print 'Firsts median', firsts.totalwgt_lb.median()
print 'Others median', others.totalwgt_lb.median()

print 'Firsts standard deviation', firsts.totalwgt_lb.std()
3# 1.4205728777207374
print 'Others standard deviation', others.totalwgt_lb.std()
## 1.3941954762143138



def CohenEffectSize(group1, group2):
	diff = group1.mean() - group2.mean()
	var1 = group1.var()
	var2 = group2.var()
	n1, n2 = len(group1), len(group2)
	pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
	d = diff / math.sqrt(pooled_var)
	return diff

effect1 = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
# -0.12476118453549034
print 'Cohen Effect Size for totalwgt_lb',effect1

## The Cohen effect size in weights is only 0.125 standard deviations 

## The same test for pregnancy length :
# prglngth - name of column
print ' '
print 'Length of pregnancy stats:'
print 'Firsts mean', firsts.prglngth.mean()
## 38.60095173351461
print 'Others mean', others.prglngth.mean()
## 38.52291446673706
print 'Others standard dev', others.prglngth.std()
## 2.615852350439255
print 'Firsts standard dev', firsts.prglngth.std()
## 2.7919014146686947

effect2 = CohenEffectSize(firsts.prglngth, others.prglngth)
## 0.07803726677754952
print 'Cohen Effect Size for prglngth', effect2


