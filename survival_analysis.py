"""
Description: survival analysis template in python 
Author: Michael Berk
Date: Winter 2021

"""

# Kaplan Meier: univariate non-parametric model that is good at developing a baseline fit
from lifelines import KaplanMeierFitter

time_to_event = [9,2,7,4,3,7,2]
event = [1,0,1,1,0,0,0]


kmf = KaplanMeierFitter()
kmf1 = kmf.fit(time_to_event, event)

kmf1.survival_function_.plot() #(ci_show=False)
plt.title('Title')

