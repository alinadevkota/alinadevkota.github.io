import pandas as pd

file_name = "experience"

# Read TSV
tsv_file = f'{file_name}.tsv'
df = pd.read_csv(tsv_file, sep='\t')

# Save as CSV
csv_file = f'{file_name}.csv'
df.to_csv(csv_file, index=False)
