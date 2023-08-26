# viet-goodreads

Welcome to the viet-goodreads project! This project aims to train a model that predicts a book's rating using the provided dataset. The project includes exploratory analysis of the data, feature engineering and selection, model training and evaluation, and deployment. 

## Team Members
- Anh Bui
- Kim Duy Nguyen
- Rhosane Santos
- Thu Thao Pham

## Getting Started

To clone the project into your local computer, follow the steps below:

1. Open your terminal or command prompt.
2. Change the current working directory to the location where you want to clone the project.
3. Run the following command:

```
git clone https://github.com/rhowsane/viet-goodreads.git
```

4. The project will be cloned to your local machine.

## Make your own branch to work on

1. Open your terminal or command prompt.
2. Change the current working directory to the location where your project is.
3. Run the following command:

```
git checkout -b dev-yourname
```
4. You are now working on your own branch. To switch back to the main branch, run the following command:

```
git checkout main
```

5. To switch back to your own branch, run the following command:

```
git checkout dev-yourname
```

6. To push your work to your own branch, run the following command:

```
git add .
git commit -m "your commit message"
git push origin dev-yourname
```

7. To merge your work to the main branch, run the following command: (MAKE SURE TO ASK FOR PERMISSION FIRST)

```
git checkout main
git merge dev-yourname
```

8. To delete your own branch, run the following command:

```
git branch -d dev-yourname
```

## Project Structure

The project repository has the following structure:

```python
viet-goodreads/
├── Dataset/
│   └── books.csv (The data is now cleaned from the original project's file)
│
├── Notebook/
│   └── clean_csv.ipynb (This notebook is to run only once to clean part of the CSV to make the file readable)
│   └── main.ipynb (This is the main notebook, including the data exploration, analysis, machine learning, etc. parts)
│   └── Dockerfile
│   └── inference.py (It was copied into the image when it wass builded)
│   └── test_df.csv (It is necessary in order to run the container from the DockerHub)
|
└── README.md
└── docker_steps.md
└── requirements.txt
└── copy_csv.py (to copy the raw data set CSV to the CSV that we will work on, so that we will always have the original csv file)

```

- The `Dataset/` directory contains the dataset file `books_raw.csv` that contains the original dataset. When you execute the copy_csv.py, a `books.csv` will be created as a clone of the `books_raw.csv`
- The `README.md` file provides an overview of the project and instructions for cloning the repository.

## Usage

Note: Make sure to install the necessary dependencies mentioned in the requirements.txt file before running them.  

To install the dependencies, run the following command:

```python
pip install -r requirements.txt
```

IMPORTANT:

If you decide to rerun the project from start to finish, here are the steps:

1. Delete the Dataset/books.csv file
2. Run the copy_csv.py file, this will create a new Dataset/books.csv file (copy of the original Dataset/books_raw.csv file)
3. Run the clean_csv.ipynb file, this will clean the Dataset/books.csv file (only need to run once, don't run it again)
4. Run the main.ipynb file, this will run the whole project from start to finish
