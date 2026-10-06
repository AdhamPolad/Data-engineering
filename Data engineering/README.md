\# Data Ingestion Project



\## Project Description



This project is a simple data ingestion and data cleaning pipeline developed using Python and Pandas.



The dataset used in this project is the IMDb Top 1000 Movies dataset downloaded from Kaggle.



The original dataset is stored in the `data/raw/` directory and is not manually modified. All data cleaning and processing operations are performed programmatically using Python.



\## Dataset



The dataset contains information about 1000 IMDb movies, including:



\* Movie title

\* Release year

\* Certificate

\* Runtime

\* Genre

\* IMDb rating

\* Overview

\* Meta score

\* Director

\* Stars

\* Number of votes

\* Gross revenue



\## Project Structure



```text

data\_ingestion\_project/

│

├── data/

│   ├── raw/

│   │   └── imdb\_top\_1000.csv

│   │

│   └── processed/

│       └── imdb\_top\_1000\_clean.csv

│

├── src/

│   └── data\_ingestor/

│       ├── \_\_init\_\_.py

│       └── cli.py

│

├── .gitignore

├── requirements.txt

└── README.md

```



\## Technologies



\* Python

\* Pandas



\## Data Processing and Cleaning



The program performs the following operations:



1\. Reads the CSV dataset using Pandas.

2\. Displays the number of rows and columns.

3\. Displays column names.

4\. Displays the first 5 rows.

5\. Displays data types.

6\. Displays missing values for each column.

7\. Cleans column names by removing leading and trailing spaces, converting names to lowercase, and replacing spaces with underscores.

8\. Removes completely empty rows.

9\. Detects and removes duplicate rows.

10\. Handles missing values in the `certificate` column by replacing them with `Unknown`.

11\. Filters movies with an IMDb rating of 8.0 or higher.

12\. Displays the number of rows before and after filtering.

13\. Saves the processed dataset to the `data/processed/` directory.



\## Dataset Results



Original dataset:



\* Rows: 1000

\* Columns: 16



Cleaning results:



\* Completely empty rows: 0

\* Duplicate rows: 0

\* Missing values in `certificate`: 101

\* Missing `certificate` values are replaced with `Unknown`.



Filtering results:



\* Rows before filtering: 1000

\* Rows after filtering: 463

\* Filter condition: IMDb rating >= 8.0



Some missing values remain in columns such as `meta\_score` and `gross` because the project handles missing values in the selected `certificate` column.



\## How to Run



\### 1. Create a virtual environment



```bash

python -m venv .venv

```



\### 2. Activate the virtual environment



On Windows PowerShell:



```powershell

.venv\\Scripts\\Activate.ps1

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the data ingestion and cleaning program



```bash

python src/data\_ingestor/cli.py --input data/raw/imdb\_top\_1000.csv --output data/processed/imdb\_top\_1000\_clean.csv

```



The processed dataset will be saved to:



```text

data/processed/imdb\_top\_1000\_clean.csv

```



