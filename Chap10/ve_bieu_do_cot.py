import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
incomes = np.array([39.6, 47.2, 55.4, 66.6, 45.7, 96.3, 54.8, 80.1, 72.5, 60.4, 74.6, 98.5])
index = np.arange(len(months))
plt.bar(months,incomes,color=['red','blue'])
plt.title('Thu nhap 2025')
plt.xticks(months,months)
plt.xlabel('Tháng')
plt.ylabel('Thu nhập')
# fig , ax = plt.subplots()
# ax.set_title('Thu nhập 2025')
# ax.bar(index, incomes, color=['#800080', '#5d3fd3'])
# ax.set_ylabel('Thu nhập')
# ax.set_xlabel('Tháng')
# ax.bar_label(ax.containers[0])
# ax.set_xticks(index, months)
# # set figure size
# fig.set_figwidth(7)
# fig.set_figheight(5)
# # set figure title
# f = pl.gcf()
# f.canvas.manager.set_window_title('My Income')
# # add grid
# plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()
