import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movie_metadata.csv')

# Dataset Info
print(df.info())
print("\nFirst few rows of the data:")
print(df.head())

# Analysis
print("\nAverage IMDB score:", df['imdb_score'].mean())
print("Most common genres:")
print(df['genres'].value_counts().head())

# To save plots
def save_plot(filename):
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Saved: {filename}")

# IMDB Score Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['imdb_score'], kde=True)
plt.title('Distribution of IMDB Scores')
plt.xlabel('IMDB Score')
save_plot('imdb_score_distribution.png')

# Budget vs Gross Earnings
plt.figure(figsize=(12, 6))
sns.scatterplot(x='budget', y='gross', data=df)
plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget')
plt.ylabel('Gross Earnings')
save_plot('budget_vs_gross.png')

# Top 10 Movies by Money Made
top_10_gross = df.nlargest(10, 'gross')
plt.figure(figsize=(12, 6))
sns.barplot(x='gross', y='movie_title', data=top_10_gross)
plt.title('Top 10 Movies by Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Movie Title')
save_plot('top_10_gross.png')

# Avg. IMDB Score by Genre
df['main_genre'] = df['genres'].apply(lambda x: x.split('|')[0])
genre_scores = df.groupby('main_genre')['imdb_score'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
genre_scores.plot(kind='bar')
plt.title('Average IMDB Score by Main Genre')
plt.xlabel('Genre')
plt.ylabel('Average IMDB Score')
plt.xticks(rotation=45)
save_plot('genre_scores.png')

# Movie Duration Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['duration'], kde=True)
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
save_plot('duration_distribution.png')

# IMDB Score vs. Movie Duration
plt.figure(figsize=(10, 6))
sns.scatterplot(x='duration', y='imdb_score', data=df)
plt.title('IMDB Score vs. Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('IMDB Score')
save_plot('score_vs_duration.png')

print("\nAll visualizations have been saved as PNG files.")