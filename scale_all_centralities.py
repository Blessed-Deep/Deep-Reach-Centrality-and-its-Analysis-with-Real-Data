import pandas as pd
from sklearn.preprocessing import StandardScaler

corona_dt = pd.read_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_data.xlsx")

corona_column_names = [column for column in corona_dt.columns if column not in ['Node', 'corona_nodes']]
scaler = StandardScaler()

corona_scaled_columns = scaler.fit_transform(corona_dt[corona_column_names])


corona_scaled_df = pd.DataFrame(corona_scaled_columns, columns=corona_column_names)

corona_scaled_df['Node'] = corona_dt['Node']
corona_scaled_df['corona_nodes'] = corona_dt['corona_nodes']


corona_scaled_df = corona_scaled_df[['Node', 'corona_nodes'] + corona_column_names]

corona_scaled_df.to_excel("outputs/centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx",index=False)

corona_scaled_df