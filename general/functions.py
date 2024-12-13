import logging
import pandas as pd
from pandas import DataFrame


class BasicDataDHandelFunctions:
    def load_dataset(file_path):
        """Loads a dataset from a specified path."""
        try:
            df = pd.read_csv(file_path)
            logging.info(f"Dataset loaded successfully from {file_path}")
            return df
        except FileNotFoundError:
            logging.error(f"File not found at {file_path}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")


    def save_dataset_csv(df, output_path='final_dataset.csv'):
        """Saves the processed DataFrame to a CSV file."""
        df.to_csv(output_path, index=False)
        logging.info(f"Final dataset saved to '{output_path}'")

