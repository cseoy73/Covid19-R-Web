from matplotlib import pyplot as plt

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Air_transport = [-0.2, -33.1, -60.7, -65.3, -60, -65, -64.8, -65.4, -63.5, -60.9]
Accommodation = [-2.2, -14.6, -32.1, -20, -10.1, -8.7, -9.1, -16.9, -21.2, -15.1]
Restaurant = [-2.1, -12.7, -28.6, -24.6, -13.9, -12.2, -7.5, -15.5, -18.8, -13.5]
Cultural_Sports = [2.7, -16.6, -45.9, -45.4, -40.4, -35.2, -30.1, -36.8, -35, -29.8]

plt.plot(month, Air_transport, marker="o")
plt.plot(month, Accommodation, marker="o")
plt.plot(month, Restaurant, marker="o")
plt.plot(month, Cultural_Sports, marker="o")

plt.xlabel('Month')
plt.ylabel('%')
plt.title('Service industry Trend')

plt.legend(['Air_transport', 'Accommodation', 'Restaurant', 'Cultural_Sports'])
plt.show()
