[![news](/pics/header.png)](/vids/News_video.mp4?raw=true)  
 
#### Table of Contents  

[Project Overview](#project-overview)  
[Resources](#resources)  
[Objectives](#objectives)  
[Summary](#summary)  
[Recommendation](#recommendation)  
[Limitations](#limitations)  
[Sources](#sources)  
[Communication Protocols](#communication-protocols)  
[Project Roadmap](#project-roadmap )  

## Project Overview  
### **Reason the topic was selected**  
**There are many articles written about Californian’s  leaving due to the high cost of living. There are many news clips, like the ones we chose for our video embedded in our header. The reason this topic was selected, with our group living in California, it's personal. We live throughout the state, Southern California to Northern California, with a wide range of interests, backgrounds, experiences. We find commonality in the abiding weight in questioning, "Is it time to leave California?"**   

As a broad generalization, most people can afford to purchase a house worth about **3X** their **total (gross) annual income**, assuming a **20% down** payment and a moderate amount of other long-term debts, such as car or student loan payments. This best practice can be found at [mymoneyblog.com](https://www.mymoneyblog.com/4-different-rules-of-thumb-for-how-much-house-you-can-afford.html). As there are many similar "Best Practices" in home buying, We would like to keep a consistency throughout the analysis and use this one, three times total annual income. The consistency will make the analysis meaningful. 

With the best practice in mind and the median price of homes currently, as of 02/13/20, listed in San Bernardino County is **$350,000**, according to [zillow.com](https://www.zillow.com/san-bernardino-county-ca/home-values/), a single gross income of **$116,666.67** would be needed to purchase a **median price** home in **San Bernardino County**.  

Although, that number is flabbergasting enough, it fails when compared to surrounding California counties. These counties the median home prices are, easily, **doubled**.  Meaning, the gross annual income would, also, have to **double**.  
Pricing can be seen on [laalmanac.com](http://www.laalmanac.com/economy/ec37.php)  

**We performed analysis on the cost of housing in California that included**:  
- Median Home Price
- Median Household Income  

**Questions the team answers with the data**  
- What are the California median household prices in California expected to be in the next five years?  
- What are the California median household prices in California expected to be in the next ten years?  
- Based on the ["Best Practices"](https://www.mymoneyblog.com/4-different-rules-of-thumb-for-how-much-house-you-can-afford.html) in home buying, how much income would be needed to live in a median priced home in California at that time?  
- What are the top 5 states Californians are moving to?  
- How does California housing cost compare to those 5 states?  

**After our analysis, we answer:**
- Is it time to leave California?  

## Resources  
- **Software:** Jupyter Notebook, PostGreSQL,   
- **Languages:** Python, JSON, SQL  
- **Dependencies:** Pandas, Matplotlib, SciPy, NumPy, Scikit-learn, hvplot, Plotly express  
- **Algorithms:** K-means, Random Forest Classifier, LinReg 
- **Data Source:** csv resources for our analysis were downloaded from [data.census.gov](https://data.census.gov), [www2.census.gov](https://www2.census.gov), and [zillow.com](https://www.zillow.com/)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2010_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2010&tid=ACSST1Y2010.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2010](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2010/state-to-state-migration/state_to_state_migrations_table_2010.xls)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[population_data](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/national/totals/nst-est2019-alldata.csv?#)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2011_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2011&tid=ACSST1Y2011.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2011](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2012/state-to-state-migration/state_to_state_migrations_table_2012.xls)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[zillow_data](https://www.zillow.com/research/data/)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2012_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2012&tid=ACSST1Y2012.S2506&=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2012](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2012/state-to-state-migration/state_to_state_migrations_table_2012.xls)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2013_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2013&tid=ACSST1Y2013.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2013](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2013/state-to-state-migration/state_to_state_migrations_table_2013.xls)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2014_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2014&tid=ACSST1Y2014.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2014](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2014/state-to-state-migration/State_to_State_Migrations_Table_2014.xls)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2015_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2015&tid=ACSST1Y2015.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2015](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2015/state-to-state-migration/State_to_State_Migrations_Table_2015.xls)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2016_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2016&tid=ACSST1Y2016.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2016](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2016/state-to-state-migration/State_to_State_Migrations_Table_2016.xls)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2017_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2017&tid=ACSST1Y2017.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2017](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2017/state-to-state-migration/State_to_State_Migrations_Table_2017.xls)  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2018_data](https://data.census.gov/cedsci/table?g=0100000US.04000.001&y=2018&tid=ACSST1Y2018.S2506&t=Financial%20Characteristics%3AHousing%3AHousing%20Value%20and%20Purchase%20Price%3AIncome%20%28Households,%20Families,%20Individuals%29%3AIncome%20and%20Earnings%3AIncome%20and%20Poverty%3AMortgage%20Costs&vintage=2018&hidePreview=true&moe=false)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[migration_2018](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2018/state-to-state-migration/State_to_State_Migrations_Table_2018.xls)  

## Objectives  
- Import, analyze, clean, and preprocess a “real-world” classification dataset  
- Select, design, and train a binary classification model for Deep Learning  
- Optimization methodology to increase model performance  

## Summary  
[Machine Learning Model](#machine-learning-model)  
[Database Integration](#database-integration)  
[Analysis](#analysis)  
[Dashboard](#dashboard)  
[Presentation](#presentation)  

## Machine Learning Model  
[Data Preprocessing](#data-preprocessing)  
[Feature Engineering](#feature-engineering)  
[Training and Testing Sets](#training-and-testing-sets)  
[Model Choice](#model-choice)  
[Model Limitations](#model-limitations)  
[Model Benefits](#model-benefits)  
[Changes In Model's Choice](#changes-in-model-choice)  
[How the Model Was Trained](#how-the-model-was-trained)  
[Model’s Confusion Matrix](#model’s-confusion-matrix)  
[Back to top](#table-of-contents)  
[Next Section](#recommendation)

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

## Analysis  
### Description of the analysis phase of the project  
One way we can tell stories with data is through interactive maps, which is what we created in our dashboard.  

The purpose of this map is to visually show the number of people moving out of California by year and the differences in these numbers by States receiving Californian migrants.  

A map was well suited for our project as the project is location-based. For stakeholders or our audience, a map visualization of where Californians are migrating and in what numbers is critical for understanding the core of the project and also visually appealing.  

To complete this project, we use selected data from our CSV and retrieve a list of geographical coordinates or centers from census.gov website. Then add the data to a map.  

Usually, to map multiple points a URL is used because the data is usually inaccessible or too large. But for this project the data for which we wanted visualized was not nearly as large.  

Our approach was to use the JavaScript and the D3.js library to retrieve the coordinates. We use the Leaflet library to plot the data on a Mapbox map through an API request. Next, we create an index.html page adding to it Leaflet CSS and JavaScript files. Then we create a style.css file which is necessary for setting specific height and style for the map on our index.html. The next step is to tell our index.html page to use the syle.css file by adding the CSS link in the head of the index.html file.  

Two other essential pieces needed includes the config.js and logic.js files. The config.js file holds the Mapbox API key, while the logic.js file will contain all the JavaScript and Leaflet code to create the map and add data to the map.  

In the step following, it is essential to allow our index.html file to use the logic.js and config.js scripts. To do this, we add our scripts to the body of the index.html file. Next, we add a circleMarker() function to the map via Leaflet.  

The last step is to add multiple markers or points to the map. To add a marker for each location or state receiving greater than 10,000 CA migrants in 2018, we iterate through the array of longitudes and latitudes and add each to the map. For best practice, we save the states array in an external file and refer to that file and dataset in the logic.js file. Finally, to add data from each object in the cities array we use Leaflet’s bindPopup() method on the marker() function.
<img align="right" width="700" src="/Data/leaf_map_here.png"><br/>  

### Database Integration
**Our final segment includes a fully integrated database, with the following features:**  
[Stores Static Data](#stores-static-data)  
[Interfaces](#interfaces)  
[Tables](#tables)  
[Joins](#joins)  
[Connection string](#connection-string)  
[Entity Relationship Diagram (ERD)](#entity-relationship-diagram-(ERD))  
[Back to top](#table-of-contents)  
[Next Section](#recommendation)  

## Stores Static Data  
Once a clean data was obtained, parsed and sorted, it made it clear what types of tables could be useful for the project. Tables were then built in PostgreSQL to store static data. An ERD with a schema was first constructed and helped shape how and what questions we wanted the database to answer or insights to generate. Eventually, multiple tables were built to store static data.  

## Interfaces  
The database interfaces with our python notebook file where all the data loading and cleaning occurred. This was achieved by importing create_engine form sqlaclchemy; the information that sqlaclchemy needs to create a database engine.  

## Tables  
Multiple tables were generated to store static data as the project evolved. Tables include combined_ca_data, ca_analysis, housing_and_income, analysis_info, just to mention a few. For example, the ca_analysis table stores static data of all CA who moved to selected states between a given period, ordered by ascending order. Similarly, the analysis_info table stores median housing cost(monthly) data for all states.  

## Joins  
A left join using the database is performed on selected states from 2017 and 2018, left joining on the States which is a column found in both data sets.  

## Connection string  
A connection string using SQLAlchemy connects our python to our PostgreSQL.  

## Entity Relationship Diagram (ERD)  
<img align="center" width="400" src="/Data/Migration_FlowDB(2).png"><br/>
<br/>
<br/>
<br/>
<br/>  

## Dashboard
The dashboard presents a data story that is logical and easy to follow for someone unfamiliar with the topic. It includes all of the following:
- Images from the initial analysis
- Data (images and report) from the machine learning task
- Interactive elements
- Our dashboard is published on GitPages [Leaving California Dashboard]()  

## Presentation  
The presentation can be found at [Google Slides](https://docs.google.com/presentation/d/14h7wNLqN1Vh8AVsPMiOpv18YU4jbhMqiKdh0yhPtdns/edit?usp=sharing)  

## Recommendation
**Recommendation for future analysis**

A linear regression was performed using the census data for 2010-2018 as well as the Zillow monthly data from April 1996 to January 2020. These regression equations were very different from each other, mainly due to the amount of information that was available in each dataset. Future analysis could include comparing the home values in the upcoming months to see if either model was close to reality. Another venue for future analysis would be to perform similar linear regressions for the other 49 US states to see if any of those models are an accurate representation of the home values in the near future. Even more interesting would be to see how the inclusion of market fluctuations in the Zillow data will hold up when predicting home values in 2030 and beyond.

As for the RandomForest Classifier, it would be interesting to see if the model could accurately predict good and bad housing costs with data from the 2020 census.

**Anything the team would have done differently**

Our original plan was to gather data from 1980 through now, to be able to show the fluctuations in home value. We had also hoped to show that the cost of housing and annual income has increased, but not at the same rates and not at sustainable rates. However, the datasets that were available on the census.gov website only went as far back as 2010. If given more time, it might have been possible to get access to previous years and convert it into datasets that were similar to the 2010-2018 data.

## Limitations  
The creating of the migration flow map requires registration for a [Mapbox](https://www.mapbox.com/) account to generate an API key to allow rendering of maps on the browser. Mapbox does provide a free tier on their [pricing]( https://www.mapbox.com/pricing/), however a credit card is required for the sign up.  

## Sources  
**DBD created at : [quickdatabasediagrams.com](https://www.quickdatabasediagrams.com/)**  

**README.md video** was created with clips from: 
- [California faces housing 'crisis' amid extremely high rents](https://www.youtube.com/watch?v=kJH4wSW_X5A)
- [California housing crisis reaches boiling point](https://www.youtube.com/watch?v=Q4Zq5NmoWoM)
- [Can Big Tech Curb A Housing Crisis It Helped Cause](https://www.youtube.com/watch?v=e-cT0gQQsiw)
- [Goodbye, California! Longtime residents fleeing rising housing cost](https://www.youtube.com/watch?v=Q4t7GlCs2IY)  

**README.md header picture** was found at:
- [zerohedge.com](https://www.zerohedge.com/political/conservative-californians-leaving-droves-america-first-law-and-order-red-states)  

**Interactive map created with** [websitebeaver.com](https://websitebeaver.com/how-to-make-an-interactive-and-responsive-svg-map-of-us-states-capitals) **| Permissible** [License](https://github.com/WebsiteBeaver/interactive-and-responsive-svg-map-of-us-states-capitals/blob/master/LICENSE)  

**Code pictures** were screenshots of:  
- [.ipynb]()  
- [.ipynb]()  
- [.ipynb]()  

## Communication Protocols  
It is important to establish a communication protocol. We created direct messages for only team members in Slack at [final-project-jas](https://ucbdatasept19.slack.com/archives/CTXNA5K5G) and exchanged cell phone numbers where we created a group-text.  

- Instant communication will be done via text  
- Ideas and links will be done via Slack  
- Meetups will be held via Zoom  

In an emergency we will inform our group through our group-text and reach out to the staff by direct conversation in Slack.  

## Project Roadmap  
The project roadmap and description of all the project deliverables can be found in [Deliverables.md](/Deliverables.md)  

[Back to top](#table-of-contents)
