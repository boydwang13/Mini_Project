# Mini_Project

## 1. Project Overview

This mini project is aiming at finding the relations between the price of a hotel and its distance to city center.

## 2. Folder Structure
```
.
├── config.yaml  #
├── data
│   ├── processed
│   │   └── hotel_vienna_munged.csv
│   └── raw
│       └── hotel_vienna_restricted.csv
├── docs
│   └── Report_about_the_output.ipynb  #some indications from the output
├── LICENSE
├── notebooks
│   └── 01_eda.ipynb   #Exploratory Data Analysis of the raw data
├── output
│   └── Scatter_Prices_VS_Distance.png
├── README.md
├── requirements.txt
└── src
    └── main.py
```

## 3. Software and Hardware Requirements


* **Language**: Python 3.9
* **Main Packages**:
    * os
    * pandas
    * matplotlib.pyplot



## 4. How to Reproduce the Results

Please follow the steps below to reproduce the results.

### Step 1: Clone the Repository

```bash
git clone https://github.com/boydwang13/Mini_Project.git
cd Mini_project
```

### Step 2: Set Up the Environment

Using Conda (recommended):
```bash
conda env create -f config.yaml
conda activate vienna-hotel-env  
```

Or,Using pip:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Code

```bash
python src/main.py
```

## 5. Data Availability and Provenance

The raw data are from [OSF](https://osf.io/).

## 6. License

This project adopts the MIT License. For detailed information about the license, please refer to the LICENSE file.
