folder_path_1 = 'E:\Documents\BU\Prof Grace Lab\xrotor\APC4_2x2';
name_1 = 'APC4_2x2';
csv_file_path_1 = sprintf('%s\\%s_data.csv', folder_path_1, name_1);
df_1 = readtable(csv_file_path_1);

folder_path_2 = 'E:\Documents\BU\Prof Grace Lab\xrotor\APC4_2x2';
name_2 = 'UIUC_APC4_2x2';
csv_file_path_2 = sprintf('%s\\%s_data.csv', folder_path_2, name_2);
df_2 = readtable(csv_file_path_2);

rpms = unique(df_1.RPM);

ind = 1;

for i = 1:length(rpms)
    figure(ind);
    ind = ind + 1;

    pltTitle_1 = sprintf('%d %s XROTOR vs Experimental Ct', rpms(i), name_1);

    filtered_df_1 = df_1(df_1.RPM == rpms(i), :);
    filtered_df_2 = df_2(df_2.RPM == rpms(i), :);

    scatter(filtered_df_1.J, filtered_df_1.Ct, 'DisplayName', 'XROTOR');
    hold on;
    scatter(filtered_df_2.J, filtered_df_2.Ct, 'DisplayName', 'Experimental');
    hold off;
    legend('Interpreter', 'none');
    title(pltTitle_1, 'Interpreter', 'none');
    grid on
    xlabel('J')
    ylabel('Ct')
    fig_name = sprintf('%d %s Ct.jpg', rpms(i), name_1);
    saveas(gcf, fig_name);

    figure(ind);
    ind = ind + 1;

    pltTitle_2 = sprintf('%d %s XROTOR vs Experimental Cp', rpms(i), name_1);
    scatter(filtered_df_1.J, filtered_df_1.Cp, 'DisplayName', 'XROTOR');
    hold on;
    scatter(filtered_df_2.J, filtered_df_2.Cp, 'DisplayName', 'Experimental');
    hold off;
    legend('Interpreter', 'none');
    title(pltTitle_2, 'Interpreter', 'none');
    grid on
    xlabel('J')
    ylabel('Cp')
    fig_name = sprintf('%d %s Cp.jpg', rpms(i), name_1);
    saveas(gcf, fig_name);
end
