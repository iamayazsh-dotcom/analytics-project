import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATA
# ============================================================

print("========== SALES INTELLIGENCE ANALYZER ==========\n - analysis.py:9")

print("Pandas Version: - analysis.py:11")
print(pd.__version__)

df = pd.read_csv(r"C:\Users\ayazs\Downloads\sales_data.csv")


# ============================================================
# 2. UNDERSTAND THE DATA
# ============================================================

print("\n========== DATASET OVERVIEW ==========\n - analysis.py:21")

print("First 5 Rows: - analysis.py:23")
print(df.head())

print("\nShape: - analysis.py:26")
print(df.shape)

print("\nColumns: - analysis.py:29")
print(df.columns.tolist())

print("\nData Types: - analysis.py:32")
print(df.dtypes)

print("\nInformation: - analysis.py:35")
df.info()

print("\nStatistical Summary: - analysis.py:38")
print(df.describe())


# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\n========== DATA CLEANING ==========\n - analysis.py:46")

print("Missing Values: - analysis.py:48")
print(df.isnull().sum())

print("\nDuplicate Rows: - analysis.py:51")
print(df.duplicated().sum())

# Remove missing values
df_cleaned = df.dropna()

# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

print("\nRows before cleaning: - analysis.py:60", len(df))
print("Rows after cleaning: - analysis.py:61", len(df_cleaned))


# ============================================================
# 4. DATA TRANSFORMATION
# ============================================================

# Revenue = Quantity × Price
df_cleaned["Revenue"] = (
    df_cleaned["Quantity"] * df_cleaned["Price"]
)

print("\n========== CREATED REVENUE ==========\n - analysis.py:73")

print(
    df_cleaned[
        ["Product", "Quantity", "Price", "Revenue"]
    ].head()
)


# ============================================================
# 5. KEY BUSINESS METRICS
# ============================================================

total_revenue = df_cleaned["Revenue"].sum()
average_revenue = df_cleaned["Revenue"].mean()

maximum_revenue = df_cleaned["Revenue"].max()
minimum_revenue = df_cleaned["Revenue"].min()

total_quantity = df_cleaned["Quantity"].sum()
average_quantity = df_cleaned["Quantity"].mean()

average_price = df_cleaned["Price"].mean()


print("\n========== KEY BUSINESS METRICS ==========\n - analysis.py:98")

print("Total Revenue: - analysis.py:100", round(total_revenue, 2))
print("Average Revenue per Order: - analysis.py:101", round(average_revenue, 2))
print("Maximum Order Revenue: - analysis.py:102", round(maximum_revenue, 2))
print("Minimum Order Revenue: - analysis.py:103", round(minimum_revenue, 2))

print("Total Quantity Sold: - analysis.py:105", total_quantity)
print("Average Quantity per Order: - analysis.py:106", round(average_quantity, 2))
print("Average Product Price: - analysis.py:107", round(average_price, 2))


# ============================================================
# 6. PRODUCT ANALYSIS
# ============================================================

revenue_by_product = (
    df_cleaned
    .groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

quantity_by_product = (
    df_cleaned
    .groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)


print("\n========== PRODUCT ANALYSIS ==========\n - analysis.py:129")

print("Revenue by Product: - analysis.py:131")
print(revenue_by_product)

print("\nQuantity Sold by Product: - analysis.py:134")
print(quantity_by_product)


# ============================================================
# 7. REGION ANALYSIS
# ============================================================

revenue_by_region = (
    df_cleaned
    .groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


print("\n========== REGION ANALYSIS ==========\n - analysis.py:150")

print("Revenue by Region: - analysis.py:152")
print(revenue_by_region)


# ============================================================
# 8. CATEGORY ANALYSIS
# ============================================================

average_price_by_category = (
    df_cleaned
    .groupby("Category")["Price"]
    .mean()
    .sort_values(ascending=False)
)

quantity_by_category = (
    df_cleaned
    .groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)


print("\n========== CATEGORY ANALYSIS ==========\n - analysis.py:175")

print("Average Price by Category: - analysis.py:177")
print(average_price_by_category)

print("\nQuantity Sold by Category: - analysis.py:180")
print(quantity_by_category)


# ============================================================
# 9. CUSTOMER ANALYSIS
# ============================================================

revenue_by_customer_type = (
    df_cleaned
    .groupby("Customer_Type")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


print("\n========== CUSTOMER ANALYSIS ==========\n - analysis.py:196")

print("Revenue by Customer Type: - analysis.py:198")
print(revenue_by_customer_type)


# ============================================================
# 10. BEST PERFORMERS
# ============================================================

best_product = revenue_by_product.idxmax()
best_region = revenue_by_region.idxmax()
best_category = quantity_by_category.idxmax()
best_customer_type = revenue_by_customer_type.idxmax()


print("\n========== BUSINESS INSIGHTS ==========\n - analysis.py:212")

print("Best Product: - analysis.py:214", best_product)
print("Best Region: - analysis.py:215", best_region)
print("Best Category by Quantity: - analysis.py:216", best_category)
print("Best Customer Type: - analysis.py:217", best_customer_type)


# ============================================================
# 11. VISUALIZATION
# ============================================================

# -------- Revenue by Product --------

plt.figure(figsize=(8, 5))

revenue_by_product.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -------- Revenue by Region --------

plt.figure(figsize=(8, 5))

revenue_by_region.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -------- Quantity by Product --------

plt.figure(figsize=(8, 5))

quantity_by_product.plot(kind="bar")

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -------- Revenue by Customer Type --------

plt.figure(figsize=(8, 5))

revenue_by_customer_type.plot(kind="bar")

plt.title("Revenue by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================================
# 12. FINAL REPORT
# ============================================================

print("\n============================================ - analysis.py:288")
print("FINAL SALES REPORT - analysis.py:289")
print("============================================ - analysis.py:290")

print("Total Revenue: - analysis.py:292", round(total_revenue, 2))
print("Total Quantity Sold: - analysis.py:293", total_quantity)
print("Average Order Revenue: - analysis.py:294", round(average_revenue, 2))

print("\nBest Product: - analysis.py:296", best_product)
print("Best Region: - analysis.py:297", best_region)
print("Best Category: - analysis.py:298", best_category)
print("Best Customer Type: - analysis.py:299", best_customer_type)

print("\n============================================ - analysis.py:301")
print("ANALYSIS COMPLETE - analysis.py:302")
print("============================================ - analysis.py:303")