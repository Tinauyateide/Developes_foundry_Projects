import numpy as np
import matplotlib.pyplot as plt

y_true = np.array([1, 2, 3, 4, 100])
y_predicted = np.array([1, 2, 3, 4, 5])

squared_error = (y_true - y_predicted) ** 2
absolute_error = np.abs(y_true - y_predicted)
print("Squared Error: ", squared_error)
print("Absolute Error: ", absolute_error)

mse = np.sum(squared_error) / len(squared_error)
mae = np.sum(absolute_error) / len(absolute_error)
print("Mean Squared Error (MSE): ", mse)
print("Mean Absolute Error (MAE): ", mae)

# Plotting the errors in a bar
plt.figure(figsize=(10, 6)) 
x_labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Outlier']
plt.bar(range(len(y_true)), squared_error, alpha=0.6, label='Squared Error', color='blue')
plt.bar(range(len(y_true)), absolute_error, alpha=0.6, label='Absolute Error', color='orange')
plt.xlabel('Data Point Index')
plt.ylabel('Error Value')
plt.title('Comparison of Squared Error and Absolute Error')
plt.legend()
plt.savefig('individual_errors_bar_chart.png')

#  Pie chart for MSE
plt.figure(figsize=(10, 6))
plt.pie(squared_error, labels=x_labels, autopct='%1.1f%%', startangle=90)
plt.title('Contribution of each Data Point to Total MSE Loss')
plt.savefig('mse_contribution_pie_chart.png') 

# Pie chart for MAE
plt.figure(figsize=(10, 6))
plt.pie(absolute_error, labels=x_labels, autopct='%1.1f%%', startangle=90)
plt.title('Contribution of each Data Point to Total MAE Loss')
plt.savefig('mae_contribution_pie_chart.png') 
