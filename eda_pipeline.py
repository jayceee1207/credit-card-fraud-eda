import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
from github import Github  
from github.GithubException import GithubException

def load_and_clean_data(filepath):
    print(">>> Initializing Data Ingestion...")
    
    # 1. Load the dataset
    try:
        df = pd.read_csv(filepath)
        print(f"SUCCESS: Dataset loaded. Dimensions: {df.shape[0]} rows, {df.shape[1]} columns.")
    except FileNotFoundError:
        print(f"ERROR: Could not find {filepath}. Please check the file name and location.")
        return None

    print("\n>>> Running Data Integrity Checks...")
    
    # 2. Check for missing (null) values
    total_missing = df.isnull().sum().sum()
    if total_missing == 0:
        print("PASS: No missing values detected.")
    else:
        print(f"WARNING: Found {total_missing} missing values. Handling required.")
        df = df.dropna() 

    # 3. Check for exact duplicate rows
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"WARNING: Found {duplicate_count} duplicate rows. Removing duplicates...")
        df = df.drop_duplicates()
        print(f"UPDATE: New Dimensions: {df.shape[0]} rows, {df.shape[1]} columns.")
    else:
        print("PASS: No duplicate rows detected.")

    print("\n>>> Data Cleaning Complete.")
    return df

# --- Main Execution Block ---
if __name__ == "__main__":
    FILE_PATH = "creditcard.csv" 
    
    # Run Phase 1 & 2
    clean_df = load_and_clean_data(FILE_PATH)
    
    if clean_df is not None:
        print("\nClass Distribution (0 = Valid, 1 = Fraud):")
        print(clean_df['Class'].value_counts())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # <-- NEW: This lets Python create folders on your Mac

def load_and_clean_data(filepath):
    print(">>> Initializing Data Ingestion...")
    try:
        df = pd.read_csv(filepath)
        print(f"SUCCESS: Dataset loaded. Dimensions: {df.shape[0]} rows, {df.shape[1]} columns.")
    except FileNotFoundError:
        print(f"ERROR: Could not find {filepath}. Please check the file name and location.")
        return None

    print("\n>>> Running Data Integrity Checks...")
    total_missing = df.isnull().sum().sum()
    if total_missing == 0:
        print("PASS: No missing values detected.")
    else:
        df = df.dropna() 

    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"WARNING: Found {duplicate_count} duplicate rows. Removing duplicates...")
        df = df.drop_duplicates()
    else:
        print("PASS: No duplicate rows detected.")

    print(">>> Data Cleaning Complete.")
    return df

# --- NEW: Phase 3 EDA Function ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # <-- NEW: This lets Python create folders on your Mac

def load_and_clean_data(filepath):
    print(">>> Initializing Data Ingestion...")
    try:
        df = pd.read_csv(filepath)
        print(f"SUCCESS: Dataset loaded. Dimensions: {df.shape[0]} rows, {df.shape[1]} columns.")
    except FileNotFoundError:
        print(f"ERROR: Could not find {filepath}. Please check the file name and location.")
        return None

    print("\n>>> Running Data Integrity Checks...")
    total_missing = df.isnull().sum().sum()
    if total_missing == 0:
        print("PASS: No missing values detected.")
    else:
        df = df.dropna() 

    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"WARNING: Found {duplicate_count} duplicate rows. Removing duplicates...")
        df = df.drop_duplicates()
    else:
        print("PASS: No duplicate rows detected.")

    print(">>> Data Cleaning Complete.")
    return df

# --- NEW: Phase 3 EDA Function ---
def perform_eda_and_save_plots(df):
    print("\n>>> Starting Exploratory Data Analysis...")
    
    # 1. Create an images folder if it doesn't exist yet
    os.makedirs("images", exist_ok=True)
    
    # 2. Plot 1: The Target Imbalance
    print("Generating Class Distribution Plot...")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Class', data=df, palette='Set2')
    plt.title('Class Distribution (0: Valid | 1: Fraud)')
    plt.savefig('images/class_distribution.png')
    plt.close() # Closes the plot so it doesn't eat up your Mac's memory
    
    # 3. Plot 2: Transaction Amounts (Fraud vs Valid)
    print("Generating Amount Distribution Plot...")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Class', y='Amount', data=df, palette='Set1')
    plt.title('Transaction Amount Distribution by Class')
    plt.yscale('log') # We use a log scale because some transactions are massive
    plt.savefig('images/amount_distribution.png')
    plt.close()

    # 4. Plot 3: Correlation Heatmap
    print("Generating Correlation Heatmap (This might take a few seconds)...")
    plt.figure(figsize=(12, 10))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, cmap='coolwarm', cbar=True, annot=False)
    plt.title('Feature Correlation Heatmap')
    plt.savefig('images/correlation_heatmap.png')
    plt.close()
    
    print(">>> EDA Complete. All plots saved to the 'images/' folder.")

# --- Main Execution Block ---
if __name__ == "__main__":
    FILE_PATH = "creditcard.csv" 
    
    # Run Phase 1 & 2
    clean_df = load_and_clean_data(FILE_PATH)
    
    if clean_df is not None:
        print("\nClass Distribution (0 = Valid, 1 = Fraud):")
        print(clean_df['Class'].value_counts())
        
        # Run Phase 3
        perform_eda_and_save_plots(clean_df)


# --- Main Execution Block ---
if __name__ == "__main__":
    FILE_PATH = "creditcard.csv" 
    
    # Run Phase 1 & 2
    clean_df = load_and_clean_data(FILE_PATH)
    
    if clean_df is not None:
        print("\nClass Distribution (0 = Valid, 1 = Fraud):")
        print(clean_df['Class'].value_counts())
        
        # Run Phase 3
        perform_eda_and_save_plots(clean_df)

# --- NEW: Phase 4 Auto-README Generation ---
def generate_readme(df):
    print("\n>>> Generating dynamic README.md...")
    
    # Calculate some dynamic stats to inject into the text
    total_transactions = len(df)
    total_frauds = df['Class'].sum()
    fraud_percentage = (total_frauds / total_transactions) * 100
    
    # Create the Markdown text template
    readme_content = f"""# Credit Card Fraud Detection: Automated EDA Pipeline

This repository contains an automated Exploratory Data Analysis (EDA) pipeline built in Python.

## Dataset Overview
* **Total Transactions:** {total_transactions:,}
* **Fraudulent Transactions:** {total_frauds:,}
* **Fraud Rate:** {fraud_percentage:.3f}%

This is a highly imbalanced dataset, which requires specialized handling and visualization techniques.

## Key Visualizations

### 1. The Class Imbalance
As seen below, the target variable is massively skewed.
![Class Distribution](images/class_distribution.png)

### 2. Transaction Time Density
Comparing when normal vs. fraudulent transactions occur.
![Time Distribution](images/time_distribution.png)

### 3. Feature Separation (V14)
Principal Component V14 shows distinct separation between valid and fraudulent distributions, making it a strong predictor for machine learning models.
![V14 Distribution](images/v14_distribution.png)

---
*Note: This README and all plots were generated entirely via a Python automation script.*
"""

    # Write the string to an actual Markdown file
    with open("README.md", "w") as file:
        file.write(readme_content)
        
    print(">>> SUCCESS: README.md created!")

# --- Main Execution Block ---
if __name__ == "__main__":
    FILE_PATH = "creditcard.csv" 
    
    # Run Phase 1 & 2
    clean_df = load_and_clean_data(FILE_PATH)
    
    if clean_df is not None:
        # Run Phase 3
        perform_eda_and_save_plots(clean_df)
        
        # Run Phase 4
        generate_readme(clean_df)
        
        print("\n>>> ALL LOCAL PHASES COMPLETE! Ready for GitHub.")

def push_to_github(token):
    print("\n>>> Initializing GitHub Connection...")
    g = Github(token)
    user = g.get_user()
    
    repo_name = "credit-card-fraud-eda" # You can change this name if you want!
    
    # 1. Create the repository
    try:
        print(f"Creating new repository: {repo_name}...")
        repo = user.create_repo(repo_name, description="Automated EDA Pipeline for Credit Card Fraud Detection")
    except GithubException as e:
        if e.status == 422: # Status 422 means the repo already exists
            print(f"Repository '{repo_name}' already exists. Connecting to it...")
            repo = user.get_repo(repo_name)
        else:
            print(f"GitHub Error: {e.data}")
            return

    # 2. Define the files to upload (Notice we skip the massive CSV)
    files_to_upload = [
        "README.md",
        "eda_pipeline.py",
        "images/class_distribution.png",
        "images/time_distribution.png",
        "images/v14_distribution.png"
    ]
    
    print("\n>>> Uploading files to GitHub...")
    for file_path in files_to_upload:
        try:
            # Read the file from your Mac
            with open(file_path, 'rb') as file:
                content = file.read()
            
            # Check if file exists on GitHub to Update, otherwise Create
            try:
                contents = repo.get_contents(file_path)
                repo.update_file(contents.path, f"Automated update for {file_path}", content, contents.sha)
                print(f"  -> Updated {file_path}")
            except:
                repo.create_file(file_path, f"Automated upload of {file_path}", content)
                print(f"  -> Uploaded {file_path}")
                
        except FileNotFoundError:
            print(f"  -> ERROR: Could not find {file_path} locally.")

    print(f"\n>>> SUCCESS! Your project is live at: https://github.com/{user.login}/{repo_name}")

# --- Main Execution Block ---
if __name__ == "__main__":
    FILE_PATH = "creditcard.csv" 
    
    # PASTE YOUR TOKEN HERE JUST FOR THIS RUN (Keep the quotes around it)
    # WARNING: Never upload a script that has your token hardcoded in it! 
    # We will delete this line immediately after it runs successfully.
    GITHUB_TOKEN = input("Please paste your GitHub Token here and press Enter: ")
    
    clean_df = load_and_clean_data(FILE_PATH)
    
    if clean_df is not None:
        perform_eda_and_save_plots(clean_df)
        generate_readme(clean_df)
        
        # Run Phase 5
        push_to_github(GITHUB_TOKEN)
        
        print("\n>>> PIPELINE COMPLETE.")