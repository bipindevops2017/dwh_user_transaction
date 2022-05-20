# DWH Coding Solution

## Thought Process

All the Data Resembled database transaction logs, and Considering it was of 1 User.
Since the Data was nested, unbalanced and missing data, I had to Normalise it , Balanced the data and either removed 
Null values or filled it with sample values.
Updated the df with updated records adn removed unwanted records(Data filtering)

Dropping the Columns that were not usefull,removing the rows which were not meeting certain criteria like balance < 0


The Solution consist of following files:

|   File_Name   | Description                                                                                    |
|:-------------:|------------------------------------------------------------------------------------------------|
|  Solution.py  | The Python File which has the logic implemented                                                |
|  Dockerfile   | File which contains the information of building image and running python script ,along with dependencies |
| Deployment.sh | Deployment Script to create the image and launch image in local container                              |

## Execution Steps

### Requirements
Install Doker machine on your system
### Execute the following commands in local directory
```

git clone https://github.com/bipindevops2017/dwh_user_transaction.git
cd solution
sh Deployment.sh  #it will ask for location of data it will be pwd+/data/
````

The Above Code will do the following activities

1. Download a Python Image ,
2. Install `pandas` as it is required for the execution of Solution.py
3. Copy the Solution.py in the Image
4. Build the Docker Image
5. Run the Image in the Container and output the result on Console

`Summary`

It has a great set of Data to Analyse  user transactions.

Please create another branch if you want to make contribution
