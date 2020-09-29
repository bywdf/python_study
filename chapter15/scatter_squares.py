import matplotlib.pyplot as plt 


x_values = list(range(1, 1000))
y_values = [i**2 for i in x_values]
plt.scatter(x_values, y_values, c =y_values, cmap=plt.cm.Blues, s=20)


# 设置图表标题并给坐标加上标签
plt.title('squre numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记字体的大小
plt.tick_params('both', which = 'major', labelsize = 14)
plt.savefig("名字")
plt.show()
