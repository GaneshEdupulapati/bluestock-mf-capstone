import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create figure
fig, ax = plt.subplots(figsize=(10, 14))

ax.set_xlim(0, 10)
ax.set_ylim(0, 16)
ax.axis("off")

# Box positions
boxes = [
    (2, 14, 6, 1, "USER\nUser Action"),
    (2, 11.8, 6, 1, "FRONTEND\nWeb / Mobile Application"),
    (2, 9.6, 6, 1, "BACKEND / API\nBusiness Logic"),
    (2, 7.4, 6, 1, "AUTHENTICATION\nAuthentication & Authorization"),
    (2, 5.2, 6, 1, "DATABASE\nCustomer / Transaction Data"),
    (2, 3.0, 6, 1, "DATA PIPELINE\nETL / ELT • Cleaning • Transformation"),
    (2, 0.8, 6, 1, "ANALYTICS → DASHBOARD\nSQL / Python → Power BI / Tableau"),
]

# Draw boxes
for x, y, width, height, text in boxes:
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.08",
        linewidth=1.5,
        edgecolor="black",
        facecolor="white"
    )

    ax.add_patch(box)

    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold"
    )

# Draw arrows
arrow_positions = [
    (5, 14, 5, 12.85),
    (5, 11.8, 5, 10.65),
    (5, 9.6, 5, 8.45),
    (5, 7.4, 5, 6.25),
    (5, 5.2, 5, 4.05),
    (5, 3.0, 5, 1.85),
]

for x1, y1, x2, y2 in arrow_positions:
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.5
        )
    )

# Title
ax.text(
    5,
    15.5,
    "Web Application Data Flow Architecture",
    ha="center",
    va="center",
    fontsize=18,
    fontweight="bold"
)

# Save PNG
output_path = "week2/software_architecture/data_flow_diagram.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Architecture diagram created successfully!")
print("Saved to:", output_path)