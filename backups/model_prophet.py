import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.stats import pearsonr
import statsmodels.api as sm
from pmdarima import auto_arima
from statsmodels.tsa.statespace import exponential_smoothing
from statsmodels.tsa.seasonal import MSTL
from statsmodels.tsa.api import STLForecast

class ProphetModel:
    def __init__(self, merged_data):
        """
        Initialize the ProductForecast class with merged data.

        :param merged_data: DataFrame containing product sales data.
        """
        self.merged_data = merged_data
        self.all_forecasts = []

    def generate_forecasts(self):
        """
        Generates forecasts for each unique product in the dataset.
        """
        for product_id in self.merged_data['id'].unique():
            product_data = self.prepare_product_data(product_id)
            model = self.fit_prophet_model(product_data)
            product_forecast = self.create_forecast(model, product_id)
            self.all_forecasts.append(product_forecast)

        result = pd.concat(self.all_forecasts, ignore_index=True)
        self.df_all_forecasts = result

    def prepare_product_data(self, product_id):
        """
        Prepares the data for the Prophet model for a given product ID.

        :param product_id: The ID of the product.
        :return: DataFrame formatted for Prophet.
        """
        product_data = self.merged_data[self.merged_data['id'] == product_id]
        prophet_df = product_data[['day', 'sales']].rename(columns={'day': 'ds', 'sales': 'y'})
        prophet_df['floor'] = 0
        return prophet_df

    def fit_prophet_model(self, prophet_df):
        """
        Fits the Prophet model to the product data.

        :param prophet_df: DataFrame formatted for Prophet.
        :return: Fitted Prophet model.
        """
        model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
        model.fit(prophet_df)
        return model

    def create_forecast(self, model, product_id):
        """
        Creates a forecast for the given product using the fitted model.

        :param model: The fitted Prophet model.
        :param product_id: The ID of the product.
        :return: DataFrame with the product forecast.
        """
        future = model.make_future_dataframe(periods=28)
        forecast = model.predict(future)
        forecast['yhat'] = forecast['yhat'].round()
        product_forecast = forecast[['ds', 'yhat']].tail(28).rename(columns={'ds': 'day', 'yhat': 'sales'})
        product_forecast['id'] = product_id
        product_forecast_wide = product_forecast.pivot(index='id', columns='day', values='sales').reset_index()
        product_forecast_wide.columns = ['id'] + [f'F{i}' for i in range(1, 29)]
        return product_forecast_wide

    def save_forecasts_to_csv(self, filename='submission.csv'):
        """
        Saves all forecasts to a CSV file.

        :param filename: The name of the file to save the forecasts.
        """
        self.df_all_forecasts.to_csv(filename, index=False)
        
        
    
    def calculate_rmse(self, true_values_df):
        """
        Calculates the RMSE between the forecasted values and the true values.

        :param true_values_df: DataFrame containing the true sales values.
        :return: RMSE value.
        """
        all_forecasts_df = pd.concat(self.all_forecasts, ignore_index=True)
        merged_results = pd.merge(true_values_df, all_forecasts_df, on='id', how='left')

        true_values = merged_results[['id'] + [f'd_{i}' for i in range(1914, 1942)]]
        forecasted_values = merged_results[['id'] + [f'F{i}' for i in range(1, 29)]]

        true_values_arr = true_values.drop('id', axis=1).to_numpy()
        forecasted_values_arr = forecasted_values.drop('id', axis=1).to_numpy()

        rmse = np.sqrt(mean_squared_error(true_values_arr, forecasted_values_arr))
        return rmse

# Example usage:
# merged_data = pd.read_csv('your_merged_data.csv')
# forecast = ProductForecast(merged_data)
# forecast.generate_forecasts()
# forecast.save_forecasts_to_csv('submission.csv')
