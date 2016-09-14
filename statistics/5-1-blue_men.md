[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

  Exercise 5.1 In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters m = 178 cm and s = 7.7 cm for men, and m = 163 cm and s = 7.3 cm for women.
 In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.
  
  
>> If we assume that the distribution  of men's heights is normal, with a mean of 178 cm and a standard deviation of 7.7 cm, then the parameters can be described as mean = 70.08 inches and standard deviation =  3.031

>> By looking at the normal cumulative distribution function for the parameters described above, we compute that 82.24% of the male population is shorter than 6'1" and 49.96% below the minimum height.  This leaves 34.37% of the male population eligible for entry, based on height alone.
  
###  Python code below:   
--------------------------------------------------------------  
```
from scipy.stats import norm  

h_mean_in = 178 * 0.393701  
h_std_in = 7.7 * 0.393701  
print h_mean_in   
print h_std_in   

blue_min = (5 * 12) + 10  
blue_max = (6 * 12) + 1  
  
propMenUnderMax = norm.cdf(blue_max,h_mean_in,h_std_in)  
propMenUnderMin = norm.cdf(blue_min,h_mean_in,h_std_in)  
eligible = propMenUnderMax - propMenUnderMin  
    
print propMenUnderMax   
print propMenUnderMin   
print 'proportion of men whose height is eligible for blue men:'  
print eligible  

```