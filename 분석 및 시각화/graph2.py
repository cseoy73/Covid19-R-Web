from matplotlib import pyplot as plt

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
All = [-0.1, -3.4, -0.2, -2.5, -1.2, 4.1, 0.1, -3.4, 3.4, -2.7]
Mining = [-1.5, -3.7, 4.7, -6, -7, 7.2, 1.6, -0.4, 5.5, -1.2]
Service = [0.5, -3.5, -4.4, 0.5, 2.4, 2.2, 0.3, -1, 0.3, 1.2]
Construction = [0.8, -2.8, 3.6, -2.4, -3.7, -0.4, 1.5, -7.5, 5.1, -0.1]

plt.plot(month, All, marker="o")
plt.plot(month, Mining, marker="o")
plt.plot(month, Service, marker="o")
plt.plot(month, Construction, marker="o")

plt.xlabel('Month')
plt.ylabel('%')
plt.title('industrial Trend')

plt.legend(['All', 'Mining', 'Service', 'Construction'])
plt.show()
