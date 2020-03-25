# Import dependencies
import pandas as pd
import plotly.express as px
import hvplot.pandas
from sklearn.cluster import KMeans

# Load data
file_path = "../../Data/Master_CleanData_Migration.csv"
df_full_migration = pd.read_csv(file_path)
df_full_migration

# Remove Puerto Rico because has no region
df_full_migration = df_full_migration[df_full_migration['Current residence'] != 'Puerto Rico']
df_full_migration

# Separate columns of overall population and residences 1 year ago
df_migration_info = df_full_migration[['Year', 'Region', 'Current residence', 'Population (1yr ago) Est', 'Same house (1yr ago) Est',
                                      'Same state of residence (1yr ago) Est', 'Different state of residence (1yr ago) Total Est', 'Abroad(1yr ago) Est']]
df_migration_info

# Sort values by year
df_migration_info = df_migration_info.sort_values(['Year', 'Region'])
df_migration_info

# Separate US data from states
us_migration_info_df = df_migration_info[df_migration_info['Region'] == 'All']
state_migration_info_df = df_migration_info[df_migration_info['Region'] != 'All']
state_migration_info_df

# Reset index
state_migration_info_df.reset_index(drop=True, inplace=True)
# Create names DataFrame for State migration
curr_residence_df = state_migration_info_df[['Region', 'Current residence']]
curr_residence_df

# Remove Region and Current residence from State DataFrame
state_migration_info_df.drop(columns=['Region', 'Current residence'], inplace=True)
state_migration_info_df

# Begin K-means analysis
# Store values of K to plot
inertia = []
k = list(range(1,11))

# Looking for the best K
for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(state_migration_info_df)
    inertia.append(km.inertia_)

# Create the Elbow Curve
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)
df_elbow.hvplot.line(x="k", y="inertia", xticks=k, title="State Migration Elbow Curve")

# Initialize the K-means model
model = KMeans(n_clusters=5, random_state=0)
# Fit the model
model.fit(state_migration_info_df)
# Predict clusters
predictions = model.predict(state_migration_info_df)
# Create column with labels
state_migration_info_df["class"] = model.labels_
state_migration_info_df

# Plot a 2D-Scatter with x="Population (1yr ago)" and y="Different state of residence"
state_migration_info_df.hvplot.scatter(x="Population (1yr ago) Est", y="Different state of residence (1yr ago) Total Est", by="class", title='State Migration K-means')

# Plot a 3D-scatter with x="Population (1yr ago)" and y="Different state of residence"
fig = px.scatter_3d(
    state_migration_info_df,
    x="Population (1yr ago) Est",
    y="Different state of residence (1yr ago) Total Est",
    z="Same state of residence (1yr ago) Est",
    color="class",
    symbol="class",
    width=800)
fig.update_layout(
    legend=dict(x=0,y=1),
    title='State Migration')
fig.show()