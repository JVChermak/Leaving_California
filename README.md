[![news](/pics/header.png)](https://www.youtube.com/embed/5GHBWSG_ifE)
 
#### Table of Contents  

[Project Overview](#project-overview)  
[Resources](#resources)  
[Objectives](#objectives)  
[Summary](#summary)  
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

- Is it time to leave California?  

**Description of the data exploration phase of the project**  
Data selection entails making good choices about which data will be used. We encountered a problem of scale/granularity; so we increased the scale to make the comparison at a state level. Our first concept involved extracting data for our individual counties to compare against each other, then choose one county from another state to compare against our indivual results. Despite previously having access to more information, we discovered that the data available through the [data.census.gov](https://data.census.gov) website only contained data sets from 2010 to 2018. After filtering what was needed for our analysis, the amount of data remaining was not enough to provide a meaningful analysis. To overcome this obstacle we decided to broaden our analysis from four counties to all states in the U.S.. California is, now, our targeted data to compare against all the other states. This decision allowed us to determine which data will be used.  

**Description of the analysis phase of the project**  
With the vast amount of data we used for our analysis, we devoloped a "user friendly" dashboard to diplay all the information. The dashboard presents a data story that is logical and easy to follow for someone unfamiliar with the topic. It includes a Leaflet.js Application Programming Interface (API) to populate a geographical map with migration data from [www2.census.gov](https://www2.census.gov). Each states migration flow is visually represented by a circle, where a higher migration population has a larger diameter. In addition, each state has a popup marker that, when clicked, shows the population and migration for that state. We, also, have an interactive HTML map. A drop down table allows the user to select a year. The map is then updated with the year selected data, each state, when hovered on, shows the median housing cost for that state.
<br/>  

<img align="left" width="250" src="/pics/migflow2_map2018.png"><br/>
<img align="left" width="250" src="/pics/migflow2_map2018.png"><br/>
<img align="left" width="250" src="/pics/cost_map.png"><br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>  

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
### Machine Learning Model  
Click [here](/Machine%20Learning.md) for details on:  
- Data Preprocessing  
- Feature Engineering  
- Training and Testing Sets  
- Model Choice  
- Model Limitations  
- Model Benefits  
- Changes In Model's Choice  
- How the Model Was Trained  
- Model’s Confusion Matrix  

### Database Integration  
Click [here](/Database%20Integration.md) for details on:
- Static Data  
- Interface  
- Tables  
- Joins  
- Connection string  
- Entity Relationship Diagram (ERD)  

### Analysis  
Click [here](/Analysis.md) for details on:
- Jupyter Notebook Analysis  
- Machine Learning Model Analysis  
- Database Integration Analysis  
- Dashboard Visual Analysis  

### Dashboard
The dashboard presents a data story that is logical and easy to follow for someone unfamiliar with the topic. It includes the following:
- Images from the initial analysis
- Data (images and report) from the machine learning task
- Interactive elements
- Our dashboard is published on GitPages [Leaving California Dashboard]()  

### Presentation  
The presentation can be found at [Google Slides](https://docs.google.com/presentation/d/e/2PACX-1vRPRYl5EeTXoGJxJPMSvwe9Y6fMAqUzO8Dy-muM66Io3Hx2QggDBBcRvqVJm9GlAwUasHoYhnPj7QyV/pub?start=false&loop=false&delayms=10000)  

### Result of analysis

### Recommendation
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
