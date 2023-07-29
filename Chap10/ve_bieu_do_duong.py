import numpy as np
import matplotlib.pyplot as plt
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
incomes = np.array([50.6, 47.2, 55.4, 66.6, 45.7, 96.3, 54.8, 80.1, 72.5, 60.4, 74.6, 88.5])
incomes2 = np.array([29.6, 77.2, 45.4, 40.6, 40.7, 44.3, 30.8, 35.1, 38.5, 39.4, 40.6, 54.5])
plt.ylabel('Thu nhập')
plt.xlabel('Tháng')
plt.title('Thu nhập 2025')
plt.xticks(months,months)
plt.plot(months,incomes,color='blue',marker='o',ls='solid',linewidth=2,label = 'Salary')
plt.plot(months,incomes2,color='red',marker='o',ls='solid',linewidth=2,label='Youtube')
plt.grid(color='green',linestyle='--',linewidth=0.5)
plt.legend()
plt.show()