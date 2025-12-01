from tabulate import tabulate
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_pdf import PdfPages

# Generate random data
headers = ["Product", "Quantity", "Price", "Status"]
data = []
for i in range(8):
    row = [
        f"Product_{random.randint(1000, 9999)}",
        random.randint(1, 100),
        f"${random.uniform(10.0, 99.9):.2f}",
        random.choice(["Active", "Inactive"])
    ]
    data.append(row)

# Create table as text
table_text = tabulate(data, headers=headers, tablefmt="grid")

# Create PDF with matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

# Create table
table = ax.table(cellText=data, colLabels=headers, 
                cellLoc='center', loc='center',
                bbox=[0, 0, 1, 1])

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Save as PDF
plt.savefig('table_method1.pdf', bbox_inches='tight', dpi=300)
plt.close()
print("Table saved as 'table_method1.pdf'")
