import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据点
np.random.seed(0)  # 保持可复现性
x = np.random.randint(0, 200, 15)
y = 0.5 * x**2 - 20 * x + 300 + np.random.normal(0, 500, 15)  # 模拟二次关系

# 拟合多项式回归（2阶）
degree = 2
coefficients = np.polyfit(x, y, degree)
poly_func = np.poly1d(coefficients)

# 预测 x = 255 的 y 值
x_pred = 255
y_pred = poly_func(x_pred)

# 生成平滑的 x 轴数据用于绘制曲线
x_smooth = np.linspace(min(x), max(x), 100)
y_smooth = poly_func(x_smooth)

# 绘图
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_smooth, y_smooth, color='red', label=f'Polynomial Regression (deg={degree})')
plt.scatter(x_pred, y_pred, color='green', marker='x', s=100, label=f'Prediction (x=255, y={y_pred:.2f})')

plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.title("Polynomial Regression Fit")
plt.show()

# 输出预测值
print(f"Predicted value at x = {x_pred}: y = {y_pred:.2f}")
