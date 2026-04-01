import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("screenshots", exist_ok=True)

df = pd.read_csv("data/ecommerce.csv")

print("Columns:\n", df.columns)

# --- 1. CSAT ---
print("Average CSAT:", df['CSAT Score'].mean())

# --- 2. Channel ---
df['channel_name'].value_counts().plot(kind='bar', title="Channel")
plt.savefig("screenshots/channel.png")
plt.close()

# --- 3. Shift ---
df['Agent Shift'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.savefig("screenshots/shift.png")
plt.close()

# --- 4. CSAT ---
sns.histplot(df['CSAT Score'])
plt.savefig("screenshots/csat.png")
plt.close()

# --- 5. Category ---
df['Product_category'].value_counts().head(10).plot(kind='bar')
plt.savefig("screenshots/category.png")
plt.close()

# --- 6. City ---
df['Customer_City'].value_counts().head(10).plot(kind='bar')
plt.savefig("screenshots/city.png")
plt.close()

# --- 7. Price ---
sns.histplot(df['Item_price'])
plt.savefig("screenshots/price.png")
plt.close()