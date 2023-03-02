import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


length_mass = int(input("Введите длину массива:\n>>> "))
mass = [list(map(float, input().split())) for _ in range(length_mass)]
title = "Цветовая карта поперечной структуры излучения\n" \
        "count_X = {}, count_Y = {}.".format(len(mass[0]), length_mass)
mass.reverse()

ax = plt.subplot()
im = ax.imshow(mass, origin="lower", extent=[0, 140, 0, 140], interpolation="none", cmap="Greys")
plt.title(title)
plt.ylabel("Координата сканирования по оси y, мм")
plt.xlabel("Координата сканирования по оси x, мм")

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=1)

plt.colorbar(im, cax=cax)
plt.savefig('x{}y{}.png'.format(len(mass[0]), length_mass))
plt.show()
