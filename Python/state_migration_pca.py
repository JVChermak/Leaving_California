# Import dependencies
import pandas as pd
import plotly.express as px
import hvplot.pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load data
file_path = "Resources/Master_CleanData_Migration.csv"
df_full_migration = pd.read_csv(file_path)
df_full_migration

# Remove Puerto Rico because has no region
df_full_migration = df_full_migration[df_full_migration['Current residence'] != 'Puerto Rico']
df_full_migration

# Remove columns of overall population and residences 1 year ago
df_migration_regions = df_full_migration.drop(columns=['Population (1yr ago) Est', 'Same house (1yr ago) Est', 'Same state of residence (1yr ago) Est', 'Different state of residence (1yr ago) Total Est', 'Abroad(1yr ago) Est'])
df_migration_regions

# Replace all NaN in the state to state migration matrix with 0
df_migration_regions.fillna(0, inplace=True)

# Sort values by year
df_migration_regions = df_migration_regions.sort_values(['Year', 'Region'])
df_migration_regions

# Separate US data from states
us_migration_regions_df = df_migration_regions[df_migration_regions['Region'] == 'All']
state_migration_regions_df = df_migration_regions[df_migration_regions['Region'] != 'All']
state_migration_regions_df

# Reset index
state_migration_regions_df.reset_index(drop=True, inplace=True)
# Create names DataFrame for State migration
curr_residence_df = state_migration_regions_df[['Region', 'Current residence']]
curr_residence_df

# Remove Region and Current residence from State DataFrame
state_migration_regions_df.drop(columns=['Region', 'Current residence'], inplace=True)
state_migration_regions_df

# Standardize data with StandardScaler
region_migration_scaled = StandardScaler().fit_transform(state_migration_regions_df)

# Initialize PCA model
pca = PCA(n_components=3)

# Get three principal components for the region_migration data
migration_pca = pca.fit_transform(region_migration_scaled)

# Transform PCA data to a DataFrame
df_migration_pca = pd.DataFrame(data=migration_pca, columns=['PC 1', 'PC 2', 'PC 3'])
df_migration_pca

# Get the explained variance
pca.explained_variance_ratio_

# Store values of K to plot
inertia = []
k = list(range(1,11))

# Looking for the best K
for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(df_migration_pca)
    inertia.append(km.inertia_)
    
# Create the Elbow Curve
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)
df_elbow.hvplot.line(x="k", y="inertia", xticks=k, title="State to State Elbow Curve")

# Initialize the K-means model
model = KMeans(n_clusters=3, random_state=0)
# Fit the model
model.fit(df_migration_pca)
# Predict clusters
predictions = model.predict(df_migration_pca)
# Create column with labels
df_migration_pca["class"] = model.labels_
df_migration_pca.head(10)

# Plot the clusters
df_migration_pca.hvplot.scatter(
    x='PC 1',
    y='PC 2',
    hover_cols=['class'],
    by='class',
    title='State to State Migration (PCA K-means)'
)

# Plot a 3D-scatter with PCA
fig = px.scatter_3d(
    df_migration_pca,
    x="PC 1",
    y="PC 2",
    z="PC 3",
    color="class",
    symbol="class",
    width=800)
fig.update_layout(legend=dict(x=0,y=1), title='State to State Migration')
fig.show()