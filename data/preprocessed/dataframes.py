import pandas as pd
import os
print(os.getcwd())
import sys
sys.path.append(os.path.abspath(".."))

file_path = '/root/code/Vivi-dsz/value_mapping/value_mapping/data/raw/user_reviews_v01.csv'
reviews_df_full = pd.read_csv(file_path)
reviews_df_full.head()


file_path = '/root/code/Vivi-dsz/value_mapping/value_mapping/data/preprocessed/topics_newkw_thousand.csv'


reviews_df =pd.read_csv(
    file_path,
    delimiter=';',
    encoding='ISO-8859-1',
    on_bad_lines='skip',  # Optional: skip malformed lines
    engine='python'  # Required when using `on_bad_lines` with older pandas
)


review_merged_df = pd.merge(
    reviews_df,
    reviews_df_full[['reviewId', 'app']],
    on='reviewId',
    how='left'
)


review_merged_df['app'] = review_merged_df['app'].replace({"TradeRepublic": "Trade Republic"})
