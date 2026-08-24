# Sales Intelligence Analyzer

A Python sales analytics script that loads sales data, cleans the dataset, calculates revenue, reports business metrics, and creates summary charts.

## Features

- Loads sales data from a CSV file with pandas
- Displays the dataset structure, data types, and statistical summary
- Reports missing values and duplicate rows
- Removes incomplete and duplicate records
- Calculates revenue as `Quantity * Price`
- Analyzes sales by product, region, category, and customer type
- Identifies the best-performing product, region, category, and customer type
- Creates bar charts for the main sales summaries

## Requirements

- Python 3.9 or later
- pandas
- matplotlib

Install the dependencies with:

```bash
pip install pandas matplotlib
```

## Input Data

The script expects a CSV file with these columns:

- `Product`
- `Quantity`
- `Price`
- `Region`
- `Category`
- `Customer_Type`

By default, the script reads:

```text
C:\Users\ayazs\Downloads\sales_data.csv
```

To use another file, update the path in `analysis.py`:

```python
df = pd.read_csv(r"C:\path\to\sales_data.csv")
```

## Run the Analysis

From the project directory, run:

```bash
python analysis.py
```

The script prints the analysis results in the terminal and opens charts for:

- Revenue by product
- Revenue by region
- Quantity sold by product
- Revenue by customer type

Close each chart window to continue to the next chart when running in an environment where plots open separately.

## Project Structure

```text
analytics-project/
|-- analysis.py
|-- README.md
```

## Calculation

For each valid row, revenue is calculated as:

```text
Revenue = Quantity x Price
```

Rows containing missing values or exact duplicates are excluded before analysis.
if wanted to see output then comment ....😎😎😎
