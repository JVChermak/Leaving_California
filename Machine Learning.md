## Data Preprocessing  
**Data selection entails making good choices about which data will be used.**  
We encountered a problem of scale/granularity; so we increased the scale to make the comparison at a state level. Our first concept involved extracting data for our individual counties to compare against each other, then choose one county from another state to compare against our indivual results. Despite previously having access to more information, we discovered that the data available through the [data.census.gov](https://data.census.gov) website only contained data sets from 2010 to 2018. After filtering what was needed for our analysis, the amount of data remaining was not enough to provide a meaningful analysis. To overcome this obstacle we decided to broaden our analysis from four counties to all states in the U.S.. California is, now, our targeted data to compare against all the other states. This decision allowed us to determine, which data will be used.  

### **Data Selection**  
- What data is available  
- What type of data is available  
- What data is missing  
- What data can be removed  

**What data is available?** 
Vast amounts of housing, population and migration information is available on census.gov. Using Pandas in Jupyter Notebook, we can view our data as a data frame. 
<img align="left" width="700" src="/pics/df.png"><br/>
<br/>
We also found that the Zillow website has housing cost information for every month starting in April 1996. We focused on the data for California for our analysis.
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>  

**What type of data is available?** Using the **dtypes method**, we confirm the data type, which also will alert us if anything should be changed in the next step. All the columns we plan to use in our model must contain a numerical data type. Our data is all **Objects** and needs to be converted to a **numeric** data type.  

<img align="left" width="700" src="/pics/dtypes.png"><br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/> 

**What data is missing?** Next, we see if any data is missing. Unsupervised learning models can’t handle missing data. If we try to run a model on a dataset with missing data, we’ll get an error. Pandas has the **isnull() method** to check for missing values. We loop through each column, check if there are null values, sum them up, and print out a readable total. We can, easily, read through our output and see there are **no** null values in our dataset. 

<img align="left" width="700" src="/pics/null_values.png"><br/>
<br/>
Once the datasets were combined for use in the machine learning models, we discovered that the census information had changed over time, creating gaps in the data for home value. Starting in 2015, there was an increase in the breakout of housing costs over $500,000 and a reduction in the categories for housing between $50,000 and $150,000. To remedy this, the groups were combined into categories that fit most of the information so that all rows and columns were still included.
<br/>
<br/>
<br/>  

**What data can be removed?** We have begun to explore the data and have taken a look at null values. Next, we determine if the data can be removed. We consider: Are there string columns that we can’t use? Are there columns with excessive null data points? Was our decision to handle missing values to just remove them?  

In the Migration Flow dataset, each row had a null data point to signify that no person migrated to the same state. For example, it doesn't make sense to say that a person migrated from Alabama to Alabama, so the value was null. Each of these values was changed to 0 for the purpose of the machine learning models. Also, because Puerto Rico was not placed into a Region, like the rest of the states, all rows for Puerto Rico were removed.

Using the **duplicated().sum() method**, we also saw our dataset did **not** have duplicates.  

<img align="left" width="700" src="/pics/duplicate.png"><br/>
<br/> 

With uncertainty of what housing data would be of value for our analysis, we went the safe route and only removed the **Margin of Error!!VALUE!!** columns. Those columns represented a margin of error for each statistic given. We felt, they would not serve a purpose for our, specific, analysis. Maybe, a complimentary analysis giving a margin of error for our analysis, at a later time. For now, we used **pandas.DataFrame.filter** to remove those columns from our data frame.  

**Data processing involves organizing the data by formatting, cleaning, and sampling it. For data processing, the focus is on making sure the data is set up for the unsupervised learning model, which requires the following:**
- Null values are handled.
- Only numerical data is used.
- Values are scaled. In other words, data has been manipulated to ensure that the variance between the numbers won’t skew results.  

**Is the data in a format that can be passed into an unsupervised learning model?**  
We saw that all our data had the incorrect type for each column. We had to use [pandas.to_numeric](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html) to convert our arguments to a numeric type. Also, we know that our model can’t have strings passed into it. The only string value left is the name of the states. 

In our dataset on state housing costs, the scale for Median Income and Median Home Value is much larger than all the other values in the dataset. We adjusted this format by dividing by 1,000 to rescale those data points.

Because values varied between single digits representing percentages to numbers representing thousands or millions of dollars, all data for the unsupervised learning models was scaled using the StandardScaler method.

### **Data Transformation**  
**Data transformation involves thinking about the future. More times than not, there will be new data coming into our data storage, with three people working on different types of data analysis. We want to make sure that whoever wants to use the data in the future can do so.**  

**Can I quickly hand off this data for others to use?**  
The data now needs to be transformed back into a more user-friendly format. We converted the final products into common data type (CSV) files. With our data being cleaned and processed, it is ready to be converted to a readable format for future use.  

We had to perform all these steps on all our datasets. We kept the process consist, not only, for us to be able to easily concatenate the years, but to have a meaningful analysis.  

The migration datasets were, also, done similarly. The most predominant change was having to add a line of code to remove the commas from the number values in order to be able to make them floats.  

## Feature Engineering
**Description of feature engineering and the feature selection, including the team’s decision-making process**  
Machine learning is the use of statistical algorithms to perform tasks such as learning from data patterns and making predictions. There are many different models; a mathematical representation of something that happens in the real world. Machine learning can be divided into three learning categories: supervised, unsupervised, and deep.  

We decided to do **supervised learning**, which deals with labeled data. This supervised learning will be used to predict, based on data from the census, whether it's time to leave California.

Additional **unsupervised learning** was done with the migration data to see if there was some unexpected groupings or patterns. Because of the number of columns that displayed state to state migrations, two methods were used to try to reduce the number of features. In one instance, the information was converted into a tall dataframe using the melt() method. For comparison's sake, another test was run with all columns reduced to three features using PCA, or principal component analysis.

## Training and Testing Sets
**Description of how data was split into training and testing sets**  
The model uses the training dataset to learn from it. It then uses the testing dataset to assess its performance. If you use your entire dataset to train the model, you won’t know how well the model will perform when it encounters unseen data. That is why it’s important to set aside a portion of your dataset to evaluate your model.
- For the linear regression and K-means models, the data was not split into training and testing sets.
- For the RandomForestClassifier, the data was split using the Scikit-learn train_test_split method using default settings.

## Model Choice
**Explanation of model choice, including limitations and benefits**  
We chose to use a Random Forest Classifier. Random Forest classifiers are a type of ensemble learning model that combines multiple smaller models into a more robust and accurate model. Random forest models use a number of weak learner algorithms (decision trees) and combine their output to make a final classification (or regression) decision.  

## Model Limitations
The limitation to us using a Random Forest model is that they will only handle tabular data, so data such as images or natural language data cannot be used without heavy modifications to the data.

## Model Benefits
Benefits to us using a random forest model are both output and feature selection are easy to interpret, and they can easily handle outliers and nonlinear data.  

## Changes In Model's Choice  
**Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)**
The main change between Segment 2 and Segment 3 was the feature engineering done to prepare for the RandomForest model. The original data does not have a target column, so one was created using a calculation of our choosing. The original calculation of monthly housing cost to monthly income ratio less than 28% only produced four "positive" outcomes all in 2010, so the model performed very well at predicting when to stay (precision 0.98, recall 0.99), but not reliably in terms of when to leave (precision 0.67, recall 0.50). Due to the number of people that have migrated from their states from 2016 on, the calculation was changed to the use of home value being less than three times the annual income. This produced a much more reasonable target column with 33 "positive" outcomes and allowed the model to train and test better.

## How the Model Was Trained  
**Description of how the model was trained (or retrained if the team used an existing model)**  
The model -> fit -> predict workflow was used on supervised and unsupervised machine learning models. The unsupervised K-means models were not trained and tested, neither was the linear regression of the housing costs in California. For the RandomForest Classifier, the data was split into the train and test sets, then the independent data was scaled using the StandardScaler fit to the X_train data. This standardizes the data, meaning that all of our numerical columns will now have a mean of 0 and a standard deviation of 1, reducing the likelihood that large values will unduly influence our model. The model was then fit to the scaled X_train and y_train data. Once the model was trained, the scaled X_test and y_test data was used to predict. 

## Model's Confusion Matrix  
**Description and explanation of model’s confusion matrix, including final accuracy score**
<img align="left" width="900" src="/pics/final_confusion_matrix.png"><br/>
<br/>
<br/>
<br/>
<br/>
<br/>

### **Models’ performance**
**The results show that:**  
- Out of **84** good housing cost (Actual 0), **84** were predicted to be good (Predicted 0), which we call true positives.  
- Out of **84** good housing cost (Actual 0), **0** was predicted to be bad (Predicted 1), which is considered a false negative. 
- Out of **33** bad housing cost (Actual 1), **1** was predicted to be good (Predicted 0) and are considered false positives.  
- Out of **33** bad housing cost (Actual 1), **32** were predicted to be bad (Predicted 1) and are considered true negatives.  
<br/>
<br/>  

##### **Precision**  
Precision is the measure of how reliable a positive classification is. From our results, the precision for the good housing cost can be determined by the ratio **TP/(TP + FP)**, which is **84/(84 + 1) = .9882**. The precision for the bad housing cost can be determined as follows: **32/(32 + 0) = 1.00**. A high precision is indicative of a low number of false positives—of the 32 housing cost we predicted to be bad housing cost, none were actually a good housing cost.
<br/> 

##### **Recall scores**  
Recall is the ability of the classifier to find all the positive samples. It can be determined by the ratio: TP/(TP + FN), or  for the good housing cost **84/(84 + 0) = 1.00** and for the bad housing cost **32/(32 + 1) = .9697**. A high recall is indicative of a low number of false negatives.
<br/>  

##### **Balanced accuracy score**  
An accuracy score is another performance metric. This program’s accuracy score appears to be great at **0.9915**.
<br/> 

##### **F1 score**  
F1 score is a weighted average of the true positive rate (recall) and precision, where the best score is 1.0 and the worst is 0.0. For classifying good housing cost, the F1 score is 0.99, while the score for classifying bad housing cost is 0.98.
<br/>  

##### **Support**  
Support is the number of actual occurrences of the class in the specified dataset. For our results, there are **84** actual occurrences for the good housing cost and **33** actual occurrences for bad housing cost.
<br/> 

##### **Recommendation on the model to use:**  
In summary, this model is good at predicting both good and bad housing cost. The model's accuracy of is high at **0.9915**, the precision and F1 score are good enough to state that the model will be good at classifying good housing cost.  

**How does the model address the question or problem the team is solving?**
While there are many factors to consider when determining if it is time to move to a different state, the model performed well at predicting if the median cost of housing is too high for the median annual income of the 50 US states from 2010 through 2018. This is by no means the final determining factor in making such a decision, but it is analysis worth looking at.