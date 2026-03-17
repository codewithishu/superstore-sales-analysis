import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load data ──────────────────────────────────────────
df = pd.read_csv('data/superstore.csv', encoding='latin-1')

# ── Clean data ─────────────────────────────────────────
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])
df['Year']       = df['Order Date'].dt.year
df['Month']      = df['Order Date'].dt.month

print("✅ Data loaded and cleaned!")

# ── 1. Sales by Category ───────────────────────────────
plt.figure(figsize=(8, 5))
cat_sales = df.groupby('Category')['Sales'].sum().sort_values()
cat_sales.plot(kind='barh', color=['#378ADD', '#1D9E75', '#BA7517'])
plt.title('Total Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('chart1_category_sales.png', dpi=150)
plt.close()
print("✅ Chart 1 saved!")

# ── 2. Monthly Sales Trend ─────────────────────────────
plt.figure(figsize=(12, 5))
monthly = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
monthly['Period'] = monthly['Year'].astype(str) + '-' + monthly['Month'].astype(str).str.zfill(2)
plt.plot(monthly['Period'], monthly['Sales'], color='#378ADD', linewidth=2, marker='o', markersize=4)
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45, ha='right', fontsize=7)
plt.tight_layout()
plt.savefig('chart2_monthly_trend.png', dpi=150)
plt.close()
print("✅ Chart 2 saved!")

# ── 3. Profit by Region ────────────────────────────────
plt.figure(figsize=(8, 5))
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
colors_r = ['#E24B4A' if x < 0 else '#1D9E75' for x in region_profit]
region_profit.plot(kind='barh', color=colors_r)
plt.title('Total Profit by Region', fontsize=14, fontweight='bold')
plt.xlabel('Total Profit ($)')
plt.tight_layout()
plt.savefig('chart3_region_profit.png', dpi=150)
plt.close()
print("✅ Chart 3 saved!")

# ── 4. Top 10 Products by Sales ────────────────────────
plt.figure(figsize=(10, 6))
top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10).sort_values()
top_products.plot(kind='barh', color='#7F77DD')
plt.title('Top 10 Products by Sales', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('chart4_top_products.png', dpi=150)
plt.close()
print("✅ Chart 4 saved!")

# ── 5. Discount vs Profit ──────────────────────────────
plt.figure(figsize=(8, 5))
plt.scatter(df['Discount'], df['Profit'], alpha=0.4, color='#D4537E', edgecolors='none')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Discount vs Profit', fontsize=14, fontweight='bold')
plt.xlabel('Discount Given')
plt.ylabel('Profit ($)')
plt.tight_layout()
plt.savefig('chart5_discount_profit.png', dpi=150)
plt.close()
print("✅ Chart 5 saved!")

# ── Key Business Insights ──────────────────────────────
print("\n" + "="*50)
print("📊 KEY BUSINESS INSIGHTS")
print("="*50)
print(f"Total Revenue   : ${df['Sales'].sum():,.0f}")
print(f"Total Profit    : ${df['Profit'].sum():,.0f}")
print(f"Profit Margin   : {(df['Profit'].sum()/df['Sales'].sum()*100):.1f}%")
print(f"Top Category    : {df.groupby('Category')['Sales'].sum().idxmax()}")
print(f"Best Region     : {df.groupby('Region')['Profit'].sum().idxmax()}")
print(f"Worst Sub-Cat   : {df.groupby('Sub-Category')['Profit'].sum().idxmin()}")
print("="*50)
print("\n✅ All done! Check your project folder for the 5 charts.")