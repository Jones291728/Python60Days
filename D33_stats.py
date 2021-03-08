from statsmodels.stats.proportion import proportions_ztest
import numpy as np
significance = 0.05
sample_failure_a, sample_size_a = (75, 300)
sample_failure_b, sample_size_b = (30, 300)

failure = np.array([sample_failure_a, sample_failure_b])
samples = np.array([sample_size_a, sample_size_b])

stat, p_value = proportions_ztest(count=failure, nobs=samples,  alternative='two-sided')
print('z_stat: %0.3f, p_value: %0.10f' % (stat, p_value))

if p_value > significance:
   print ("H1_Fail to reject the null hypothesis")
else:
   print ("H0_Reject the null hypothesis")