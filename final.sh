#!/bin/bash

# Prompt the user for the entire command
echo "run the load.py file:"
read user_command

# Run the user-specified command
eval "$user_command"

scripts=("dpre.py" "eda.py" "vis.py" "model.py")
files=("vis.png" "res_dpre.csv" "k.txt" "eda-in-1" "eda-in-2" "eda-in-3")

destination_path="C:\Users\Good User\Desktop\bd-a1\service-result"

# Run  Python scripts  and redirect to local machine
for script in "${scripts[@]}"; do
    python3 "$script"
done

# out files
for file in "${files[@]}"; do
   docker cp bd-a1-container:"/home/doc-bd-a1/$file" "$destination_path"
done

docker stop bd-a1-container