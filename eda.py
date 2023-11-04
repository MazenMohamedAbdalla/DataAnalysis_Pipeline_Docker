import load

# Load the dataset
load.r_dataset('res_dpre.csv')
data = load.call()

# Open and prepare text files for saving insights
insight_files = [open(f'eda-in-{i}.txt', 'w') for i in range(1, 4)]

# Step 1: Basic Dataset Information
# Get an overview of the dataset
num_rows, num_cols = data.shape
insight_1 = f"Example insight 1: The dataset contains {num_rows} rows and {num_cols} columns."
insight_files[0].write(insight_1)

# Step 2: Data Summary
# Get basic statistics for numerical columns
numerical_summary = data.describe()
insight_2 = "Example insight 2: Summary statistics for numerical columns:\n" + str(numerical_summary)
insight_files[1].write(insight_2)

# Step 3: Categorical Data Summary
# Get information about categorical columns
categorical_summary = data.describe(include=['object'])
insight_3 = "Example insight 3: Summary statistics for categorical columns:\n" + str(categorical_summary)
insight_files[2].write(insight_3)

# Close the insight files
for file in insight_files:
    file.close()