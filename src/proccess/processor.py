import sys
import pandas as pd

sys.path.insert(0, '../src')
from proccess.utils import get_day, get_month, get_year, get_weekday

class DataProcessor():

    def __init__(self, df):
        self._df = df

    def show_data(self) -> pd.DataFrame:
        if(self._df is None):
             raise ValueError("No data find. Call 'read_df' first.")

        print("\n    [INFO] Actual data ...")
        print(f"\n{self._df.sample(5)} ...")

    def get_data(self) -> pd.DataFrame:
        return self._df

    def save_data(self, file_path: str) -> None:
        """
        Save processed data
        """
        self._df.to_parquet(file_path)

    def remove_columns(self, column_name : str) -> None:
        """
        Remove column
        """
        self._df = self._df.drop('date', axis=1)

    def create_total_sales_column(self) -> None:   
        """
        Group and create a new column 
        """
        grouped_df = self._df.groupby(['date', 'store_id'])['price'].sum().reset_index()
        grouped_df = grouped_df.rename(columns={'price': 'total_sales'}) 

        self._df = grouped_df

    def create_weekday_column(self) -> None:
        """
        Create a weekday column
        """
        self._df['weekday'] = self._df['date'].apply(get_weekday)

    def create_day_month_year_columns(self) -> None:
        """
        Divide data column in other columns
        """
        self._df['day'] = self._df['date'].apply(get_day)
        self._df['month'] = self._df['date'].apply(get_month)
        self._df['year'] = self._df['date'].apply(get_year)

    def reorder_columns(self, column_order : list[str]) -> None:
        """
        Reorder columns order in dataframe
        """
        self._df = self._df.reindex(columns=column_order)

if __name__ == '__main__':
    
    if len(sys.argv) != 2 :
        raise ValueError(" [ USAGE ]: python3 processor.py <path-generated-data>")

    # Take arguments from console
    print("\n    [INFO] Reading data ...")
    data_original_path = sys.argv[-1]
    df = pd.read_csv(data_original_path)

    # Instantiate processor
    print("\n    [INFO] Creating DataProcessor() ...")
    processor = DataProcessor(df)
    processor.show_data()

    # Create total sales column
    print("\n    [INFO] Create total sales column ...")
    processor.create_total_sales_column()
    processor.show_data()

    # Create a weekday column
    print("\n    [INFO] Create weekday column ...")
    processor.create_weekday_column()
    processor.show_data()

    # Create day, month , year columns
    print("\n    [INFO] Create day, month , year columns ...")
    processor.create_day_month_year_columns()
    processor.show_data()

    # Drop column date:
    print("\n    [INFO] Drop column date ...")
    processor.remove_columns(column_name="date")
    processor.show_data()

    # Adjust column order:
    print("\n    [INFO] Reorder columns ...")
    column_order = ['store_id', 'year', 'month', 'day', 'weekday', 'total_sales']
    processor.reorder_columns(column_order=column_order)
    processor.show_data()

    # Save processed data
    date_original_data = data_original_path.split('train')[1][1:].split('.')[0]
    processed_data_path = "../data/train-" + date_original_data + ".parquet"

    print(f"\n    [INFO] Saving processed data in {processed_data_path} ... \n")
    processor.save_data(processed_data_path)
