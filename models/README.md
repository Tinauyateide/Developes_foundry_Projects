This folder stores serialized preprocessing and model artifacts.

Files:
- preprocessor.joblib   : scikit-learn ColumnTransformer / Pipeline used to transform input features
- best_model.joblib    : Trained scikit-learn model (estimator) for predicting "price_log" (log1p of price_lacs)

How to load and predict on new data (example):

```python
import pandas as pd
import joblib

# Load artifacts
preprocessor = joblib.load('models/preprocessor.joblib')
model = joblib.load('models/best_model.joblib')

# new_df: a pandas DataFrame with the raw features matching the original training columns
# Example: new_df = pd.read_csv('new_data.csv')

# Transform and predict (output will be log1p of price in lacs)
X_new = preprocessor.transform(new_df)
price_log_pred = model.predict(X_new)

# Convert back to original price scale
price_pred_lacs = np.expm1(price_log_pred)

print(price_pred_lacs)
```

Notes:
- Ensure new_df contains the same raw columns (names and types) used during training.
- If new categorical levels appear, the OneHotEncoder is set to ignore unknowns.
