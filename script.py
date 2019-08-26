# importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

# Configuring Pandas to display all columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# load the dataset
beers = pd.read_csv('./beers.csv')
# print(beers.head(10))

# Describe data
# print(beers.describe())
# print(beers.info())

# types of beers
# print((beers["style"].value_counts()).head(10))

# Countplot
# sns.countplot(x='style', data=beers)
# sns.countplot(x="ounces", data=beers)

# Scatter Plot
# sns.FacetGrid(beers, hue="ounces").map(plt.scatter, 'ibu', 'abv').add_legend()

# Box Plot
# ax = sns.boxplot(x="ounces", y="abv", data=beers)
# ax = sns.stripplot(x="ounces", y="abv", data=beers, jitter=True, edgecolor="gray")

# # Violin Plot
sns.violinplot(x="ounces", y="abv", data=beers, size=6)
plt.show()