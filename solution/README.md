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



To do the following tasks, you probably gonna need some kinds data processing library in your own choice of programming language.
`pandas`, a data processing library in Python, is recommended due to ease of use and simplicity. However, you are free to choose
any programming language and any framework to implement the solution.

1. Visualize the complete historical table view of each tables in tabular format in stdout (hint: print your table)
2. Visualize the complete historical table view of the denormalized joined table in stdout by joining these three tables (hint: the join key lies in the `resources` section, please read carefully)
3. From result from point no 2, discuss how many transactions has been made, when did each of them occur, and how much the value of each transaction?  
   Transaction is defined as activity which change the balance of the savings account or credit used of the card
   
## Submission

To submit your tasks, simply create the necessary implementation code in given `solution` directory.
You may want make this directory a git repository and checkpoint your work periodically here.

In addition to your core logic codebase, please also include scripts to deploy your code to a Docker container.
Your code has to be deployed in **local Docker container**. Please also include the necessary files (such as `Dockerfile` and automation scripts)
to deploy and run your code inside a Docker container.

Please also include a `README.md` inside the `solution` directory to give a summary of your submitted solution,
the thinking behind your implemented solution, and how to run your solution end-to-end in a Docker container to get the desired result as stated above. 

