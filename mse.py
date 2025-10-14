def mean_squared_error(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("The length of true values and predicted values must be the same.")

    mse = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)
    return mse

y_true = [10, 40, 60]
y_pred = [12, 48, 64]

result = mean_squared_error(y_true, y_pred)

print(result)