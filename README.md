### 🤖 SalesSage | Model Prediction

This project focuses on developing a machine learning model designed to predict the total sales for individual stores on a daily basis.

#### 📌️ How to use this project

Clone the project :

```
    git clone <this-project-github-link>
```

Create a enviroment :

```bash
    python3 -m venv venv
    source venv/bin/activate
```

Install dependencies :

```bash
    pip install -r requirements.txt
```

* **Generate Mocked Data**


To generate random data that will be used for the model, run the command:

```bash
    python3 get_data.py <year_from> <month_from> <day_from> <year_to> <month_to> <day_to>
```

The date must be created within the *data folder*.

* **What the model should predict**

The model will `predict the total to be sold per store in one day.`

The expected result is a DataFrame where each line represents the total sales of a store in one day:

* **Step by Step**

The step-by-step process followed for the development of the project can be followed in the Jupyter notebook: `notebooks/report.ipynb`

#### 📂️ Folders

* `data/` : Content all the data used or created by this project.
<br>

* `models/` : Models created by this project.
<br>

* `notebooks/` : Notebooks for data exploration. 
<br>

* `src/` : Source code for the project.

<br>
@2024, Insper. 9° Semester,  Computer Engineering.
<br>

_Machine Learning Ops & Interviews Discipline_
