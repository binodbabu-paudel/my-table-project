Random Table Generator

This project generates random data tables and exports them as PDF files.

Files
- `table_generator.ipynb` - Jupyter notebook with the table generation code
- `outputs/random_table.pdf` - Generated PDF table

How to Run
1. Clone this repository
2. Open `table_generator.ipynb` in Jupyter Notebook
3. Run all cells
4. The PDF will be generated in the `outputs/` folder

Example Output
The generated PDF contains a table like this:

| Product    | Quantity | Price  | Status   |
|------------|----------|--------|----------|
| Product_1234 | 45      | $23.45 | Active   |
| Product_5678 | 78      | $67.89 | Inactive |

Requirements
- Python 3.6+
- matplotlib
- tabulate
