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
├── test.ipynb (To be modified)
│
└── README.md
```

- The `Dataset/` directory contains the dataset file `books.csv`.
- The `README.md` file provides an overview of the project and instructions for cloning the repository.

## Usage

(To be modifed)

Note: Make sure to install the necessary dependencies mentioned in the notebooks before running them.  

If you wish, create your own development branch to keep record of your work as dev-yourname.
