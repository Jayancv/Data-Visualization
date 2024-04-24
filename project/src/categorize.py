import pandas as pd

# Read main file and subfiles
main_df = pd.read_csv("../resources/DataScience_salaries_2024.csv")
subfiles = {
    'categories/job_counts_filtered_AI.csv': 'Replacement',
    'categories/job_counts_filtered_Business.csv': 'Replacement',
    'categories/job_counts_filtered_Data.csv': 'Replacement',
    'categories/job_counts_filtered_ML.csv': 'Replacement',
    'categories/other_job_titles.csv': 'Replacement'
}
main_df['job_title'] = main_df['job_title'].str.replace(r'\bML\b', 'Machine Learning', regex=True)

# Create a dictionary to map job titles to replacements from subfiles
job_title_mapping = {}
for subfile, replacement_col in subfiles.items():
    sub_df = pd.read_csv(subfile)
    for index, row in sub_df.iterrows():
        job_title_mapping[row['job_title']] = row[replacement_col]

# Function to get replacement based on job title
def get_replacement(job_title):
    return job_title_mapping.get(job_title, job_title)

# Add replacement column to main file
main_df['Replacement'] = main_df['job_title'].apply(get_replacement)

# Write updated main file
main_df.to_csv('updated_main_file.csv', index=False)

job_counts = main_df['Replacement'].value_counts()

job_counts_df = job_counts.reset_index()
job_counts_df.columns = ['Replacement', 'count']

# Save to a new CSV file
job_counts_df.to_csv("Replacement.csv", index=False)