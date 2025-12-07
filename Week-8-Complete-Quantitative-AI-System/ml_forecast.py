# ml_forecast.py 
# Quantitative AI - Machine Learning Forecasting Module 
import pandas as pd 
import numpy as np 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
from scipy import stats 
import xgboost as xgb 
import warnings 
warnings.filterwarnings('ignore') 
class QuantitativeMLForecaster: 
    """ 
    Quantitative Machine Learning implementation for numerical forecasting 
    Applies mathematical learning algorithms from Chapters 18 & 20 
    Focus on numerical feature engineering and statistical validation 
    """ 
     
    def __init__(self, data): 
        """Initialize with quantitative dataset""" 
        self.data = data 
        self.models = {} 
        self.predictions = {} 
        self.metrics = {} 
         
        # Quantitative AI banner 
        print("\033[91m" + "="*60)  # Red 
        print("\033[97m" + "    🤖 QUANTITATIVE ML FORECASTER 🤖")  # White 
        print("\033[94m" + "="*60 + "\033[0m")  # Blue 
         
    def engineer_quantitative_features(self, window=30): 
        """Create numerical features using mathematical transformations""" 
        print("\n\033[96m📊 ENGINEERING QUANTITATIVE FEATURES...\033[0m") 
         
        df = self.data.copy() 
         
        # Lag features (autoregressive components) 
        for i in range(1, window + 1): 
            df[f'lag_{i}'] = df['volume'].shift(i) 
         
        # Statistical rolling features 
        df['rolling_mean_7'] = df['volume'].rolling(7).mean() 
        df['rolling_mean_30'] = df['volume'].rolling(30).mean() 
        df['rolling_std_7'] = df['volume'].rolling(7).std() 
        df['rolling_std_30'] = df['volume'].rolling(30).std() 
        df['rolling_min_7'] = df['volume'].rolling(7).min() 
        df['rolling_max_7'] = df['volume'].rolling(7).max() 
         
        # Mathematical transformations 
        df['log_volume'] = np.log1p(df['volume'])  # Log transformation 
        df['sqrt_volume'] = np.sqrt(df['volume'])  # Square root transformation 
        df['volume_squared'] = df['volume'] ** 2  # Polynomial feature 
         
        # Numerical time encoding 
        df['day_of_week'] = df.index.dayofweek 
        df['day_of_month'] = df.index.day 
        df['month'] = df.index.month 
        df['quarter'] = df.index.quarter 
        df['year'] = df.index.year 
        df['day_sin'] = np.sin(2 * np.pi * df.index.dayofyear / 365) 
        df['day_cos'] = np.cos(2 * np.pi * df.index.dayofyear / 365) 
         
        # Binary indicators (mathematical step functions) 
        df['is_weekend'] = (df['day_of_week'] >= 5).astype(int) 
        df['is_month_end'] = (df.index.day > 25).astype(int) 
         
        # Linear time index for trend 
        df['time_index'] = range(len(df)) 
         
        # Drop NaN rows from lag features 
        df = df.dropna() 
         
        print(f"✓ Engineered {len(df.columns)-1} quantitative features") 
        print(f"✓ Feature dimensionality: {df.shape[1]-1}") 
        print(f"✓ Sample size: {len(df)} observations") 
         
        return df 
    
    def prepare_ml_features(self):
        """Prepare features for training and forecasting."""
        try:
            # If features already engineered and cached
            if hasattr(self, 'feature_df') and self.feature_df is not None:
                return self.feature_df
        except AttributeError:
            pass
        # Engineer features and cache
        self.feature_df = self.engineer_quantitative_features()
        return self.feature_df
     
    def train_models(self, test_size=90): 
        """Train multiple ML models""" 
        print("\n\033[93m🎓 TRAINING ML MODELS...\033[0m") 
         
        # Prepare features 
        df = self.prepare_ml_features() 
         
        # Split features and target 
        feature_cols = [col for col in df.columns if col != 'volume'] 
        X = df[feature_cols] 
        y = df['volume'] 
         
        # Time series split (no shuffle!) 
        train_size = len(X) - test_size 
        X_train, X_test = X[:train_size], X[train_size:] 
        y_train, y_test = y[:train_size], y[train_size:] 
         
        # 1. Linear Regression (baseline ML) 
        print("\n  📈 Training Linear Regression...") 
        self.models['linear'] = LinearRegression() 
        self.models['linear'].fit(X_train, y_train) 
        linear_pred = self.models['linear'].predict(X_test) 
        linear_mae = mean_absolute_error(y_test, linear_pred) 
        print(f"     MAE: {linear_mae:.2f}") 
         
        # 2. Random Forest (ensemble method from Ch 18) 
        print("\n  🌲 Training Random Forest...") 
        self.models['rf'] = RandomForestRegressor( 
            n_estimators=100,  
            max_depth=10, 
            random_state=42 
        ) 
        self.models['rf'].fit(X_train, y_train) 
        rf_pred = self.models['rf'].predict(X_test) 
        rf_mae = mean_absolute_error(y_test, rf_pred) 
        print(f"     MAE: {rf_mae:.2f}") 
         
        # 3. XGBoost (gradient boosting) 
        print("\n  🚀 Training XGBoost...") 
        self.models['xgb'] = xgb.XGBRegressor( 
            n_estimators=100, 
            max_depth=5, 
            learning_rate=0.1, 
            random_state=42 
        ) 
        self.models['xgb'].fit(X_train, y_train) 
        xgb_pred = self.models['xgb'].predict(X_test) 
        xgb_mae = mean_absolute_error(y_test, xgb_pred) 
        print(f"     MAE: {xgb_mae:.2f}") 
         
        # Store test predictions 
        self.test_predictions = { 
            'actual': y_test, 
            'linear': linear_pred, 
            'rf': rf_pred, 
            'xgb': xgb_pred 
        } 
         
        # Feature importance (Random Forest) 
        print("\n\033[92m📊 TOP 5 IMPORTANT FEATURES:\033[0m") 
        importance = pd.DataFrame({ 
            'feature': feature_cols, 
            'importance': self.models['rf'].feature_importances_ 
        }).sort_values('importance', ascending=False).head(5) 
         
        for idx, row in importance.iterrows(): 
            bar = '█' * int(row['importance'] * 100) 
            print(f"  {row['feature']}: {bar} {row['importance']:.3f}") 
         
        return self.models 
     
    def forecast_future(self, periods=13*30):  # 13 months 
        """Generate future forecasts""" 
        print("\n\033[95m🔮 GENERATING 13-MONTH FORECAST...\033[0m") 
         
        # Prepare current features 
        df = self.prepare_ml_features() 
        feature_cols = [col for col in df.columns if col != 'volume'] 
         
        # Initialize forecast storage 
        forecasts = { 
            'linear': [], 
            'rf': [], 
            'xgb': [] 
        } 
         
        # Use last known features as starting point 
        last_features = df[feature_cols].iloc[-1:].copy() 
         
        # Generate forecasts iteratively 
        for i in range(periods): 
            # Update time-based features 
            future_date = df.index[-1] + pd.Timedelta(days=i+1) 
            last_features['day_of_week'] = future_date.dayofweek 
            last_features['day_of_month'] = future_date.day 
            last_features['month'] = future_date.month 
            last_features['quarter'] = future_date.quarter 
            last_features['is_weekend'] = int(future_date.dayofweek >= 5) 
            last_features['is_month_end'] = int(future_date.day > 25) 
            last_features['time_index'] = last_features['time_index'] + 1 
             
            # Make predictions 
            for model_name, model in self.models.items(): 
                pred = model.predict(last_features)[0] 
                forecasts[model_name].append(pred) 
             
            # Update lag features with ensemble prediction 
            ensemble_pred = np.mean([ 
                forecasts['linear'][-1], 
                forecasts['rf'][-1], 
                forecasts['xgb'][-1] 
            ]) 
             
            # Shift lag features 
            for lag in range(30, 1, -1): 
                if f'lag_{lag}' in last_features.columns: 
                    last_features[f'lag_{lag}'] = last_features[f'lag_{lag-1}'].values 
            last_features['lag_1'] = ensemble_pred 
         
        # Create forecast DataFrame 
        future_dates = pd.date_range( 
            start=df.index[-1] + pd.Timedelta(days=1), 
            periods=periods, 
            freq='D' 
        ) 
         
        self.forecast_df = pd.DataFrame({ 
            'date': future_dates, 
            'linear': forecasts['linear'], 
            'rf': forecasts['rf'], 
            'xgb': forecasts['xgb'] 
        }) 
         
        # Add ensemble forecast 
        self.forecast_df['ensemble'] = self.forecast_df[['linear', 'rf', 'xgb']].mean(axis=1) 
         
        # Add confidence intervals (using std of models) 
        self.forecast_df['lower_bound'] = self.forecast_df['ensemble'] - self.forecast_df[['linear', 'rf', 'xgb']].std(axis=1) * 1.96 
        self.forecast_df['upper_bound'] = self.forecast_df['ensemble'] + self.forecast_df[['linear', 'rf', 'xgb']].std(axis=1) * 1.96 
         
        # Monthly aggregation 
        self.monthly_forecast = self.forecast_df.set_index('date').resample('M').agg({ 
            'ensemble': 'sum', 
            'lower_bound': 'sum', 
            'upper_bound': 'sum' 
        }) 
         
        print(f"✓ Generated {periods} daily forecasts") 
        print(f"✓ Aggregated to {len(self.monthly_forecast)} monthly forecasts") 
        return self.forecast_df 
