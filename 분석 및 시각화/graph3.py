from matplotlib import pyplot as plt

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Employment = [26800, 27991, 26609, 26562, 26930, 27055, 27106, 27085, 27012, 27088, 27241]
Unemployment = [1153, 26838, 1180, 1172, 1278, 1228, 1138, 864, 1000, 1028, 967]

plt.plot(month, Employment, marker="o")
plt.plot(month, Unemployment, marker="o")

plt.xlabel('Month')
plt.ylabel('단위: 천(명)')
plt.title('Employment And Unemployment')
plt.legend(['Employment', 'Unemployment'])
plt.show()