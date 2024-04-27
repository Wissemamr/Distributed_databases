from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
from io import StringIO


DEBUG: bool = False

# Load the iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target
if DEBUG:
    print(iris_df.tail())


# create an empy csv file
csv_data = StringIO()
# append the data to the csv file
iris_df.to_csv(csv_data, index=False)


# getfalue() is used to get the content of the csv file
csv_content = csv_data.getvalue()
# now let's save the content to a file
with open("data\\iris.csv", "w") as f:
    f.write(csv_content)
    print("File saved successfully")


if DEBUG:
    # Load the iris dataset from the csv file
    iris_df = pd.read_csv("iris.csv")
    print(f"*** iris.csv of shape {iris_df.shape} loaded successfully ***")


# XML to JSON
# convert an xml file to json