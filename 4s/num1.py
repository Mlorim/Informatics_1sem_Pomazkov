lt.subplot(2, 2, i+1)

x = np.arange(0, 5, 0.25)
y = [i ** i for i in x]

plt.plot(x, y, '+', label='x^x')

plt.title('Exponent', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.xlabel('X')
plt.ylabel('X^X')

plt.legend()
plt.show()
