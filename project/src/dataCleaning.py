import pandas as pd


df = pd.read_csv("../resources/DataScience_salaries_2024.csv")

df['job_title'] = df['job_title'].str.replace(r'\bML\b', 'Machine Learning', regex=True)


# Group by job_title and count occurrences
job_counts = df['job_title'].value_counts()

job_counts_df = job_counts.reset_index()
job_counts_df.columns = ['job_title', 'count']

# Save to a new CSV file
job_counts_df.to_csv("job_counts.csv", index=False)


filtered_AI_df = df[df['job_title'].str.contains(r'AI|Artificial', case=False)]
filtered_ML_df = df[df['job_title'].str.contains(r'ML|Machine Learning', case=False)]
filtered_Data_df = df[df['job_title'].str.contains(r'Data', case=False)]
filtered_Business_df = df[df['job_title'].str.contains(r'Business', case=False)]
# Combine all filtered DataFrames
filtered_job_titles = pd.concat([filtered_AI_df, filtered_ML_df, filtered_Data_df, filtered_Business_df])
other_job_titles_df = df[~df.index.isin(filtered_job_titles.index)]

# Group by job_title and count occurrences
job_counts_AI = filtered_AI_df['job_title'].value_counts()
job_counts_ML = filtered_ML_df['job_title'].value_counts()
job_counts_Data = filtered_Data_df['job_title'].value_counts()
job_counts_Business = filtered_Business_df['job_title'].value_counts()
job_counts_other = other_job_titles_df['job_title'].value_counts()



# Convert Series to DataFrame
job_counts_AI_df = job_counts_AI.reset_index()
job_counts_AI_df.columns = ['job_title', 'count']

job_counts_ML_df = job_counts_ML.reset_index()
job_counts_ML_df.columns = ['job_title', 'count']

job_counts_Data_df = job_counts_Data.reset_index()
job_counts_Data_df.columns = ['job_title', 'count']

job_counts_Business_df = job_counts_Business.reset_index()
job_counts_Business_df.columns = ['job_title', 'count']

job_counts_other_df = job_counts_other.reset_index()
job_counts_other_df.columns = ['job_title', 'count']



# Save to a new CSV file
job_counts_AI_df.to_csv("job_counts_filtered_AI.csv", index=False)
job_counts_ML_df.to_csv("job_counts_filtered_ML.csv", index=False)
job_counts_Data_df.to_csv("job_counts_filtered_Data.csv", index=False)
job_counts_Business_df.to_csv("job_counts_filtered_Business.csv", index=False)


# Save other job titles to a new CSV file
job_counts_other_df.to_csv("other_job_titles.csv", index=False)

