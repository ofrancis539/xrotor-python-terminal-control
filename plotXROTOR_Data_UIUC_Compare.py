import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

name_1 = "APC9x6"
folder_path_1 = 'E:\\Documents\\BU\\Prof Grace Lab\\xrotor\\APC9x6'
csv_file_path_1 = '%s\\%s_Vel_Sweep_data.csv' % (folder_path_1,name_1)

df_1 = pd.read_csv(csv_file_path_1)

name_2 = "UIUC_APC9x6"
folder_path_2 = 'E:\\Documents\\BU\\Prof Grace Lab\\xrotor\\APC9x6'
csv_file_path_2 = '%s\\%s_Vel_Sweep_data.csv' % (folder_path_2,name_2)

df_2 = pd.read_csv(csv_file_path_2)

rpms = df_1.RPM.unique()


ind = 1
for rpm in rpms:

    fig = plt.figure(ind)
    ind = ind+1

    pltTitle_1 = "%d %s XROTOR vs Experimental Ct" % (rpm,name_1)
    
    filtered_df_1 = df_1[df_1['RPM'] == rpm]
    filtered_df_2 = df_2[df_2['RPM'] == rpm] 

    plt.scatter(filtered_df_1['J'],filtered_df_1['Ct'],label = 'XROTOR')
    plt.scatter(filtered_df_2['J'],filtered_df_2['Ct'],label = 'Experimental')
    plt.legend()
    plt.title(pltTitle_1)
    
    fig = plt.figure(ind)
    ind = ind+1

    pltTitle_2 = "%d %s XROTOR vs Experimental Cp" % (rpm,name_1)
    plt.scatter(filtered_df_1['J'],filtered_df_1['Cp'],label = 'XROTOR')
    plt.scatter(filtered_df_2['J'],filtered_df_2['Cp'],label = 'Experimental')
    plt.legend()
    plt.title(pltTitle_2)

plt.show()

