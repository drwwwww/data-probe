# 📊 Data Probe CLI

**Data Probe** is a Python terminal app that allows users to **analyze**, **calculate**, and **clean** data from a CSV file interactively — no Excel or UI required.

---

## ✅ Features

- 📁 **CSV File Input** – Load any local `.csv` file and instantly display the contents.
- 📊 **Column Analysis** – Check:
  - Data type
  - Number of unique values
  - Top 5 most frequent values
- ➗ **Numeric Calculations** – Run stats like:
  - Mean, Median, Standard Deviation
  - Min & Max
  - Count of missing (NaN) values
- 🧹 **Data Cleaning** – Drop all rows with NaNs and save a clean version to CSV.
- 🎨 **Colorized CLI** – Easy-to-read output using the `colorama` library.

---

## 💻 Installation

```bash
git clone https://github.com/drwwwww/data-probe.git
cd data-probe

pip install -r requirements.txt
# or install manually
pip install pandas numpy colorama
