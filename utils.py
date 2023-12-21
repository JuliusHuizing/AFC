import pandas as pd

import numpy as np

# 
class Data:
    def __init__(self):
        self.load_datasets()
        self.prepare_sales_data()
        self.calculate_total_sales()
        self.merge_data_and_calendar()
        self.calculate_daily_and_weekly_sales()
        self.process_unique_events()
        self.merge_calendar_and_sell_prices()
        self.merge_sales_and_sell_prices()
        self.process_holidays()
        self.create_daily_sales_df()

    def load_datasets(self):
        """Load all datasets from CSV files."""
        self.calendar = pd.read_csv("calendar_afcs2023.csv")
        self.sell_prices = pd.read_csv("sell_prices_afcs2023.csv")
        self.sales_train = pd.read_csv("sales_train_validation_afcs2023.csv")
        self.sales_test = pd.read_csv("sales_test_validation_afcs2022.csv") # Only use for testing
        self.sample_submission = pd.read_csv("sample_submission_afcs2023.csv")

    def prepare_sales_data(self):
        """Transform sales data for further analysis."""
        sales_data_long = pd.melt(self.sales_train, id_vars=['id'],
                                  var_name='day', value_name='sales')
        sales_data_long['day'] = pd.to_datetime('2011-01-29') + pd.to_timedelta(sales_data_long['day'].str[2:].astype(int) - 1, unit='D')
        self.sales_data_long = sales_data_long

    def calculate_total_sales(self):
        """Calculate total sales from the sales training dataset."""
        self.total_sales = self.sales_train.iloc[:, 1:].sum(axis=0)

    def merge_data_and_calendar(self):
        """Merge sales data with the calendar data."""
        self.calendar['date'] = pd.to_datetime(self.calendar['date'])
        self.merged_data = pd.merge(self.sales_data_long, self.calendar, left_on='day', right_on='date', how='left')

    def calculate_daily_and_weekly_sales(self):
        """Calculate daily and weekly average sales."""
        self.daily_sales = self.merged_data.groupby('day')['sales'].sum()
        self.weekly_avg_sales = self.merged_data.groupby('weekday')['sales'].mean()
        ordered_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.weekly_avg_sales = self.weekly_avg_sales.reindex(ordered_days)

    def process_unique_events(self):
        """Extract and process unique events from the calendar."""
        self.unique_events = self.calendar[['event_name_1', 'event_type_1']].drop_duplicates()

    def merge_calendar_and_sell_prices(self):
        """Merge calendar data with sell prices."""
        self.calendar_sell_merge = pd.merge(self.calendar, self.sell_prices, on='wm_yr_wk')
        self.mean_prices = self.calendar_sell_merge.groupby('date')['sell_price'].mean()

    def merge_sales_and_sell_prices(self):
        """Merge sales data with sell prices."""
        self.sales_sellprice_merge = pd.merge(self.daily_sales, self.mean_prices, left_on='day', right_on='date', how='inner')

    def process_holidays(self):
        """Process holiday events from the calendar."""
        events_df = self.calendar[['date', 'event_name_1', 'event_name_2']].dropna()
        events_df['holiday'] = events_df['event_name_1'] + ', ' + events_df['event_name_2'].fillna('')
        events_df.drop(['event_name_1', 'event_name_2'], axis=1, inplace=True)
        events_df['date'] = pd.to_datetime(events_df['date'])
        self.holidays_df = events_df[events_df['holiday'] != ''][['date', 'holiday']]
        self.holidays_df.columns = ['ds', 'holiday']
        
    def create_daily_sales_df(self):
        self.sales_test_long = pd.melt(self.sales_test, id_vars=['id'],
        var_name='day', value_name='sales')
        self.sales_test_long['day'] = pd.to_datetime('2011-01-29') + pd.to_timedelta(self.sales_test_long['day'].str[2:].astype(int) - 1, unit='D')
        self.calendar['date'] = pd.to_datetime(self.calendar['date'])
        self.merged_test_data = pd.merge(self.sales_test_long, self.calendar, left_on='day', right_on='date', how='left')
        self.daily_sales_test = self.merged_test_data.groupby('day')['sales'].sum()





import os
import pickle

# Function to extract timestamp from filename
def get_timestamp(filename):
    try:
        return int(filename.split("_")[-1].split(".")[0])
    except:
        return 

def get_most_recent_pickle_that_starts_with(prefix, directory) -> str:
    # Get a list of pickle files that start with the given prefix in the given directory
    pickle_files = [file for file in os.listdir(directory) if file.endswith(".pkl") and file.startswith(prefix)]
    # Find the most recent pickle file
    if pickle_files:
        latest_pickle_file = max(pickle_files, key=get_timestamp)
        return latest_pickle_file
    
        # Read the data from the most recent pickle file

