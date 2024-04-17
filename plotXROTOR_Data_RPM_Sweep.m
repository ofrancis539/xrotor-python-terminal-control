clear
close all

folder_path = 'E:\Documents\BU\Prof Grace Lab\xrotor';
names = {'APC4_2x2', 'APC4_2x4', 'APC9x4', 'APC9x6'};

csv_file_paths = cell(1,length(names));
df = cell(1,length(names));
for i = 1:length(names)
    csv_file_paths{i} = sprintf('%s\\%s_RPM_Sweep\\%s_RPM_Sweep_data.csv', folder_path, names{i}, names{i});
    df{i} = readtable(csv_file_paths{i});
end

figure
hold on
pltTitle_1 = sprintf('Hover RPM Sweep XROTOR Ct');
for i = 1:length(names)
    scatter(df{i}.RPM, df{i}.Ct, 'DisplayName', names{i});    
end
legend('Location','eastoutside','Interpreter', 'none');
title(pltTitle_1, 'Interpreter', 'none');
grid on
xlabel('RPM')
ylabel('Ct')
fig_name = sprintf('Hover RPM Sweep XROTOR Ct.jpg');
hold off
saveas(gcf, fig_name);

figure
hold on
pltTitle_1 = sprintf('Hover RPM Sweep XROTOR Cp');
for i = 1:length(names)
    scatter(df{i}.RPM, df{i}.Cp, 'DisplayName', names{i});    
end
legend('Location','eastoutside','Interpreter', 'none');
title(pltTitle_1, 'Interpreter', 'none');
grid on
xlabel('RPM')
ylabel('Cp')
fig_name = sprintf('Hover RPM Sweep XROTOR Cp.jpg');
hold off
saveas(gcf, fig_name);
