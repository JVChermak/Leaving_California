# Import dependencies
import pandas as pd
import plotly.express as px
import hvplot.pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load data
file_path = "../../Data/Master_CleanData_Migration.csv"
df_full_migration = pd.read_csv(file_path)
df_full_migration

# Get list of columns to move "Abroad" with other info columns
cols = df_full_migration.columns.to_list()
cols

# Reorder columns
df_full_migration = df_full_migration[['Year', 'Region', 'Current residence', 'Population (1yr ago) Est', 'Same house (1yr ago) Est', 'Same state of residence (1yr ago) Est',
 'Different state of residence (1yr ago) Total Est', 'Abroad(1yr ago) Est', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
 'District of Columbia ', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
 'Wisconsin', 'Wyoming']]
df_full_migration

# Replace all NaN in the state to state migration matrix with 0
df_full_migration.fillna(0, inplace=True)

# Remove Puerto Rico because has no region
df_full_migration = df_full_migration[df_full_migration['Current residence'] != 'Puerto Rico']
df_full_migration

# Separate US data from states
us_migration_df = df_full_migration[df_full_migration['Region'] == 'All']
state_migration_df = df_full_migration[df_full_migration['Region'] != 'All']
state_migration_df

# Unpivot data for US migrations
melted_us_migration_df = pd.melt(us_migration_df, id_vars=['Year', 'Region', 'Current residence', 'Population (1yr ago) Est', 'Same house (1yr ago) Est', 'Same state of residence (1yr ago) Est', 'Different state of residence (1yr ago) Total Est', 'Abroad(1yr ago) Est'], var_name='State_moved_to', value_name='Number_moved')
melted_us_migration_df

# Remove Region and Current residence columns
melted_us_migration_df.drop(columns=['Region', 'Current residence'], inplace=True)
# Sort data by year
melted_us_migration_df = melted_us_migration_df.sort_values('Year')

# Reset index
melted_us_migration_df.reset_index(drop=True, inplace=True)
melted_us_migration_df

# Store "State_moved_to" info in separate DF
us_states_moved_to_df = melted_us_migration_df[['Year', 'State_moved_to']]
us_states_moved_to_df

# Remove State_moved_to column
clean_us_migration_df = melted_us_migration_df.drop(columns=['State_moved_to'])
clean_us_migration_df

# Standardize data with StandardScaler
us_migration_scaled = StandardScaler().fit_transform(clean_us_migration_df)

# Initialize PCA model
pca = PCA(n_components = 3)

# Get three principal components for us migration data
us_migration_pca = pca.fit_transform(us_migration_scaled)

# Transform PCA data to a DataFrame
df_us_migration_pca = pd.DataFrame(data=us_migration_pca, columns=['PC 1', 'PC 2', 'PC 3'])
df_us_migration_pca

# Get the explained variance
pca.explained_variance_ratio_

# Store values of K to plot
inertia = []
k = list(range(1,11))

# Looking for the best K
for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(df_us_migration_pca)
    inertia.append(km.inertia_)
    
# Create the Elbow Curve
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)
df_elbow.hvplot.line(x="k", y="inertia", xticks=k, title="US Migration Elbow Curve")

# Initialize the K-means model
model = KMeans(n_clusters=2, random_state=0)
# Fit the model
model.fit(df_us_migration_pca)
# Predict clusters
predictions = model.predict(df_us_migration_pca)
# Create column with labels
df_us_migration_pca["class"] = model.labels_
df_us_migration_pca.head(10)

# Plot the clusters
df_us_migration_pca.hvplot.scatter(
    x='PC 1',
    y='PC 2',
    hover_cols=['class'],
    by='class',
    title='US Migration PCA K-means'
)

# Plot a 3D-scatter with PCA
fig = px.scatter_3d(
    df_us_migration_pca,
    x="PC 1",
    y="PC 2",
    z="PC 3",
    color="class",
    symbol="class",
    width=800)
fig.update_layout(legend=dict(x=0,y=1), title='US Migration')
fig.show()

# Unpivot data for State migrations
melted_state_migration_df = pd.melt(state_migration_df, id_vars=['Year', 'Region', 'Current residence', 'Population (1yr ago) Est', 'Same house (1yr ago) Est', 'Same state of residence (1yr ago) Est', 'Different state of residence (1yr ago) Total Est', 'Abroad(1yr ago) Est'], var_name='State_moved_to', value_name='Number_moved')
melted_state_migration_df

# Sort data by year and region
melted_state_migration_df = melted_state_migration_df.sort_values(['Year', 'Region'])
# Reset index
melted_state_migration_df.reset_index(drop=True, inplace=True)
melted_state_migration_df

# Store Region, Current residence and State_moved_to info in separate DF
states_info_df = melted_state_migration_df[['Year', 'Region', 'Current residence', 'State_moved_to']]
states_info_df

# Remove Region, Current residence and State_moved_to from melted_state_migration_df for PCA
clean_state_migration_df = melted_state_migration_df.drop(columns=['Year', 'Region', 'Current residence', 'State_moved_to'])
clean_state_migration_df

# Standardize data with StandardScaler
state_migration_scaled = StandardScaler().fit_transform(clean_state_migration_df)

# Using same PCA model as US, get three principal components for us migration data
state_migration_pca = pca.fit_transform(state_migration_scaled)

# Transform PCA data to a DataFrame
df_state_migration_pca = pd.DataFrame(data=state_migration_pca, columns=['PC 1', 'PC 2', 'PC 3'])
df_state_migration_pca

# Get the explained variance
pca.explained_variance_ratio_

# Store values of K to plot
inertia = []
k = list(range(1,11))

# Looking for the best K
for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(df_state_migration_pca)
    inertia.append(km.inertia_)
    
# Create the Elbow Curve
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)
df_elbow.hvplot.line(x="k", y="inertia", xticks=k, title="State Migration PCA Elbow Curve")

# Initialize the K-means model
model = KMeans(n_clusters=3, random_state=0)
# Fit the model
model.fit(df_state_migration_pca)
# Predict clusters
predictions = model.predict(df_state_migration_pca)
# Create column with labels
df_state_migration_pca["class"] = model.labels_
df_state_migration_pca.head(10)

# Create new DataFrame with all info
state_migration_info_df = clean_state_migration_df.merge(df_state_migration_pca, left_on=clean_state_migration_df.index, right_on=df_state_migration_pca.index)
state_migration_info_df.drop(columns=['key_0'], inplace=True)
state_migration_info_df = states_info_df.merge(state_migration_info_df, left_on=states_info_df.index, right_on=state_migration_info_df.index)
state_migration_info_df.drop(columns=['key_0'], inplace=True)
state_migration_info_df

# Plot the clusters
state_migration_info_df.hvplot.scatter(
    x='PC 1',
    y='PC 2',
    hover_cols=['class'],
    by='class',
    title='State Migration PCA K-means'
)

# Plot a 3D-scatter with PCA
fig = px.scatter_3d(
    state_migration_info_df,
    x="PC 1",
    y="PC 2",
    z="PC 3",
    color="class",
    symbol="class",
    width=800)
fig.update_layout(legend=dict(x=0,y=1), title='State Migration')
fig.show()

