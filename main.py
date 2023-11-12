import pandas as pd
import numpy as np
import os
import re

# Define the authors and the corresponding directories for their works
authors_directories = {
    'Tolstoy': '/Users/efimovivan/Desktop/Py/pythonProject1/Tolstoy/',
    'Dostoevsky': '/Users/efimovivan/Desktop/Py/pythonProject1/Dostoevsky/',
    'Chekhov': '/Users/efimovivan/Desktop/Py/pythonProject1/Chekhov/',
    'Blok': '/Users/efimovivan/Desktop/Py/pythonProject1/Blok/',
    'Gogol': '/Users/efimovivan/Desktop/Py/pythonProject1/Gogol/',
    'Pushkin': '/Users/efimovivan/Desktop/Py/pythonProject1/Pushkin/'
}

# Initialize an empty dataframe
df = pd.DataFrame(columns=['sentence', 'author'])

# Function to split text into sentences using regular expressions
def split_into_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences
print("tyrett0")

# Process each author's works
for author, directory in authors_directories.items():
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        continue

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file and not a subdirectory
        if os.path.isfile(file_path):
            # Read the text file
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Split the text into sentences
            sentences = split_into_sentences(text)

            # Filter out short sentences and add to the dataframe
            for sentence in sentences:
                if len(sentence) >= 15:
                    df = df._append({'sentence': sentence, 'author': author}, ignore_index=True)

print("tyrett1")
# Set random seed for reproducibility
np.random.seed(42)

# Define the sample sizes for each author
sample_sizes = {
    'Tolstoy': 5000,
    'Dostoevsky': 15000,
    'Chekhov': 8000,
    'Blok': 11000,
    'Gogol': 20000,
    'Pushkin': 3000
}
print("tyrett2")
# Sample the sentences for each author
sampled_df = pd.DataFrame(columns=['sentence', 'author'])
for author, size in sample_sizes.items():
    author_sentences = df[df['author'] == author]
    sample_size = min(size, len(author_sentences))  # Take the minimum of the desired size or the actual size
    sampled_sentences = author_sentences.sample(n=sample_size, random_state=42)
    sampled_df = pd.concat([sampled_df, sampled_sentences], ignore_index=True)

# Shuffle the dataset
sampled_df = sampled_df.sample(frac=1).reset_index(drop=True)

# Save the dataset to a CSV file
sampled_df.to_csv('author_sentences.csv', index=False)

print("Dataset created successfully!")




