python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = 'Pensioners_Distribution_by_Type_and_Gender_2022.csv'
data = pd.read_csv(data_path)

# Convert the 'Year' and 'Quarter' columns to a single datetime column
data['Period'] = data['Year'].astype(str) + ' Q' + data['Quarter'].astype(str)

# Filter data by gender and sum up the counts by quarter
def plot_gender_distribution(data, gender):
    filtered_data = data[data['Gender'] == gender]
    grouped = filtered_data.groupby('Period')['Count'].sum().reset_index()

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Period', y='Count', data=grouped, palette="Blues_d")
    plt.title(f'{gender} Pensioners Distribution by Quarter (2022)')
    plt.xlabel('Quarter')
    plt.ylabel('Number of Pensioners')
    plt.show()

# Example: Plot the distribution for Female pensioners
plot_gender_distribution(data, 'Female')
