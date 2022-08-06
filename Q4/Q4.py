import matplotlib.pyplot as plt

import SimpleStimulator as simp

# print(simp.x_axis)
# print(simp.y_axis)


plt.scatter(simp.x_axis,simp.y_axis)
plt.title("Memory address v/s clock cycle")
plt.xticks(simp.x_axis)
plt.yticks(simp.y_axis)
plt.xlabel("clock cycle")
plt.ylabel("Memory address")
plt.show()