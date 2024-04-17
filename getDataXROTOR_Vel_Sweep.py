import os
import pandas as pd

def extract_part_from_line(file_path, keyword, delimiter, part_index):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                parts = line.strip().split(delimiter)
                if part_index < len(parts):
                    result.append(parts[part_index])

    return result
    

name = "APC4_2x2"
folder_path = 'E:\\Documents\\BU\\Prof Grace Lab\\xrotor\\APC4_2x2'
csv_file_path = '%s\\%s_Vel_Sweep_data.csv' % (folder_path,name)

df = pd.read_csv(csv_file_path)

# List all files in the folder
files = os.listdir(folder_path)

# Loop through each file
for ind,file_name in enumerate(files):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Check if it's a file (not a subdirectory)
    if os.path.isfile(file_path) and file_path.endswith("_Vel_Sweep.dat"):

        rpmKeyword = 'rpm'
        delimiter = ':'  # Adjust based on the actual delimiter in your file
        rpmPart_index = 3   # Adjust to the index of the part you want to extract

        rpmExtracted_parts = extract_part_from_line(file_path, rpmKeyword, delimiter, rpmPart_index)
        rpmExtracted_parts = rpmExtracted_parts[0].strip().split(' ')

        JKeyword = 'J'
        delimiter = ':'  # Adjust based on the actual delimiter in your file
        JPart_index = 1   # Adjust to the index of the part you want to extract

        JExtracted_parts = extract_part_from_line(file_path, JKeyword, delimiter, JPart_index)
        JExtracted_parts = JExtracted_parts[0].strip().split(' ')

        CtKeyword = 'Ct'
        delimiter = ':'  # Adjust based on the actual delimiter in your file
        CtPart_index = 1   # Adjust to the index of the part you want to extract

        CtExtracted_parts = extract_part_from_line(file_path, CtKeyword, delimiter, CtPart_index)
        CtExtracted_parts = CtExtracted_parts[0].strip().split(' ')

        CpKeyword = 'Cp'
        delimiter = ':'  # Adjust based on the actual delimiter in your file
        CpPart_index = 2   # Adjust to the index of the part you want to extract

        CpExtracted_parts = extract_part_from_line(file_path, CpKeyword, delimiter, CpPart_index)
        CpExtracted_parts = CpExtracted_parts[0].strip().split(' ')

        # Print or process the extracted parts
        new_row = {'Name':name,'RPM':round(float(rpmExtracted_parts[0])),'J':JExtracted_parts[0], 'Ct':CtExtracted_parts[0], 'Cp':CpExtracted_parts[0]}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

df.to_csv(csv_file_path, index=False)


