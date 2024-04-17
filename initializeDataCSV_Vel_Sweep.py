import pandas as pd

# Specify column headers
name = "APC4_2x2"
column_headers = ['Name','RPM','J', 'Ct', 'Cp']

# Create an empty DataFrame with column headers
empty_dataframe = pd.DataFrame(columns=column_headers)

csv_file_path = 'E:\\Documents\\BU\\Prof Grace Lab\\xrotor\\APC4_2x2\\%s_Vel_Sweep_data.csv' % (name)
empty_dataframe.to_csv(csv_file_path, index=False)