import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook

workSheet = load_workbook("data.xlsx")["Sheet1"]
firstCloumn = []
secondCloumn = []
for i in range(1, workSheet.max_row + 1):
    firstCloumn.append(workSheet[f"A{i}"].value)

for j in range(1, workSheet.max_row + 1):
    secondCloumn.append(workSheet[f"B{j}"].value)

x = np.array(firstCloumn)
y = np.array(secondCloumn)

diff1 = 3*(x**2)
diff2 = 6*x

plt.plot(x, y)
plt.plot(x, diff1)
plt.plot(x, diff2)
plt.show()
