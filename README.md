#  Semiconductor Yield Analysis & Defect Detection

This project analyzes semiconductor wafer manufacturing data to understand yield trends, detect spatial defect patterns, and build predictive models using Python. It simulates wafer-level data and applies clustering and machine learning to uncover insights in semiconductor production.

##Personal Note
This project was created as part of a course I’m taking on Coursera, and also to support my learning as a master’s student in the semiconductor field.

 I’ll be honest — I didn’t understand all of the code at first.
I built this with the help of AI tools like ChatGPT, which guided me step by step.
 But after working through the process, I’ve gained a much better understanding of how it all works — and I’m proud of the progress I've made.

##Contact
Made by Zeyad Mustafa
Feel free to connect or contribute if you're also working in semiconductor data or machine learning!

---

## Features

-  **Yield Distribution Analysis**: Understand overall production yield patterns.
-  **Defect Type Analysis**: Analyze common defect types and their occurrence.
-  **Defect Clustering**: Use KMeans to identify spatial clusters of defects on wafer maps.
-  **Yield Prediction**: Train a Random Forest model to classify wafers as high-yield or low-yield.
-  **Modular Python Code**: Easy-to-extend scripts organized by purpose.

---

##  Project Structure

semiconductor-yield-analysis/
├── data/ # Contains CSV wafer data
│ └── sample_wafer_data.csv
├── notebooks/ # Jupyter notebooks for analysis
│ ├── 01_eda.ipynb
│ ├── 02_clustering.ipynb
│ └── 03_model.ipynb
├── src/ # Python scripts
│ └── data_loader.py
├── requirements.txt # Python dependencies
├── .gitignore # Files to exclude from Git
└── README.md # Project overview
##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/semiconductor-yield-analysis.git
   cd semiconductor-yield-analysis


pip install -r requirements.txt
