# Import dependencies
import pandas as pd
import hvplot.pandas

# Load data
file_path = "Resources/Master_CleanData_Migration.csv"
df_full_migration = pd.read_csv(file_path)

# Remove Puerto Rico because has no region
df_full_migration = df_full_migration[df_full_migration['Current residence'] != 'Puerto Rico']

# Separate columns of overall population and residences 1 year ago
df_migration_info = df_full_migration[['Year', 'Region', 'Current residence', 'Population (1yr ago) Est', 'Same house (1yr ago) Est',
                                      'Same state of residence (1yr ago) Est', 'Different state of residence (1yr ago) Total Est', 'Abroad(1yr ago) Est']]

# Separate the states moved to
df_migration_patterns = df_full_migration.drop(columns=['Population (1yr ago) Est', 'Same house (1yr ago) Est', 'Same state of residence (1yr ago) Est', 'Different state of residence (1yr ago) Total Est', 'Abroad(1yr ago) Est'])
df_migration_patterns.fillna(0, axis=1, inplace=True)

# Create DataFrame for overall migration to each state
df_us_migration = df_migration_patterns[df_migration_patterns['Region'] == 'All']
df_us_migration.sort_values('Year')

# Create DataFrame for migration to states by region
df_by_region = df_migration_patterns[df_migration_patterns['Region'] != 'All']
df_by_region = df_by_region.groupby(['Year', 'Region']).sum()
df_by_region.reset_index(inplace=True)
df_by_region

# Unpivot data so that the states are listed in a "State" column and the number of people moved is next to this.
df_by_region = pd.melt(df_by_region, id_vars=['Year', 'Region'], var_name='State_moved_to', value_name='Number_moved')

# Sort data by year and region
df_by_region.sort_values(['Year', 'Region'])

# Create region DataFrames to analyze
midwest_migration_df = df_by_region[df_by_region['Region'] == 'Midwest_states']
northeast_migration_df = df_by_region[df_by_region['Region'] == 'Northeast_states']
south_migration_df = df_by_region[df_by_region['Region'] == "South_states"]
west_migration_df = df_by_region[df_by_region['Region'] == 'West_states']

# Visually inspect West coast migration patterns
west_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Look closer into the top 5 states to migrate to, not including California
top_west_migration_df = west_migration_df[(west_migration_df['State_moved_to'] == 'Texas') | (west_migration_df['State_moved_to'] == 'Washington') | (west_migration_df['State_moved_to'] == 'Arizona') | (west_migration_df['State_moved_to'] == 'Oregon') | (west_migration_df['State_moved_to'] == 'Nevada') | (west_migration_df['State_moved_to'] == 'New York')]

# Pivot US migration data
df_us_migration.drop(columns=['Region', 'Current residence'], inplace=True)
df_us_migration = pd.melt(df_us_migration, id_vars=['Year'], var_name='State_moved_to', value_name='Number_moved')

# Arrange data to be listed by year starting in 2010 
df_us_migration = df_us_migration.sort_values('Year')
df_us_migration.reset_index(drop=True)

# Visually inspect migration for US
df_us_migration.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Take a closer look at top migration states, not including California
top_us_migration_df = df_us_migration[(df_us_migration['State_moved_to'] == 'Texas') | (df_us_migration['State_moved_to'] == 'Florida') | (df_us_migration['State_moved_to'] == 'New York') | (df_us_migration['State_moved_to'] == 'Illinois') | (df_us_migration['State_moved_to'] == 'Georgia') | (df_us_migration['State_moved_to'] == 'Virginia') | (df_us_migration['State_moved_to'] == 'Pennsylvania')]

# Visually inspect top US migration states
top_us_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Visually inspect Midwest migration patterns
midwest_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Take a closer look at the top Midwest migration states
top_midwest_migration_df = midwest_migration_df[(midwest_migration_df['State_moved_to'] == 'Illinois') | (midwest_migration_df['State_moved_to'] == 'Florida') | (midwest_migration_df['State_moved_to'] == 'Texas') | (midwest_migration_df['State_moved_to'] == 'Minnesota') | (midwest_migration_df['State_moved_to'] == 'Missouri') | (midwest_migration_df['State_moved_to'] == 'California') | (midwest_migration_df['State_moved_to'] == 'Wisonsin')]

# Visually inspect top Midwest migration patterns
top_midwest_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Visually inspect the Northeast migration patterns
northeast_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Take a closer look at the top Northeast migration states, including California
top_northeast_migration_df = northeast_migration_df[(northeast_migration_df['State_moved_to'] == 'New York') | (northeast_migration_df['State_moved_to'] == 'New Jersey') | (northeast_migration_df['State_moved_to'] == 'Florida') | (northeast_migration_df['State_moved_to'] == 'Massachusetts') | (northeast_migration_df['State_moved_to'] == 'California') | (northeast_migration_df['State_moved_to'] == 'Pennsylvania')]

# Visually inspect the top Northeast migration patterns
top_northeast_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Visually inspect the South migration patterns
south_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

# Take a closer look at the top South migration states, including California
top_south_migration_df = south_migration_df[(south_migration_df['State_moved_to'] == 'Florida') | (south_migration_df['State_moved_to'] == 'California') | (south_migration_df['State_moved_to'] == 'New York') | (south_migration_df['State_moved_to'] == 'Texas') | (south_migration_df['State_moved_to'] == 'Georgia') | (south_migration_df['State_moved_to'] == 'Virginia') | (south_migration_df['State_moved_to'] == 'North Carolina')]

# Visually inspect top South migration patterns
top_south_migration_df.hvplot.scatter(x='Year', y='Number_moved', by='State_moved_to')

