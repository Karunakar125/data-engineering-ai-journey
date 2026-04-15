import pandas as pd
df=pd.read_csv("/content/Realestate_Analysis.csv")
df.columns
srt=df.sort_values(by='Sale Amount',ascending=True)
df_amt_grtr_than_0=srt[srt['Sale Amount']>0]
unique_sale_amounts = df_amt_grtr_than_0['Sale Amount'].unique()
display(unique_sale_amounts)
###############################
# Get records with unique 'Sale Amount' values (keeping all columns)
df_unique_sale_amount_records = df_amt_grtr_than_0.drop_duplicates(subset=['Sale Amount'])

display(df_unique_sale_amount_records.head(20))
##########################
srtdf=(srt[srt['Sale Amount'].isin(unique_sale_amounts)])
srtisnull=(srtdf['Property Type'].notnull())
srtdf['CalculatedRatio']=(srtdf['Assessed Value']/srtdf['Sale Amount']).round(4)
srtdffinal=srtdf[srtdf['Property Type'].notnull()]
display(srtdffinal.head(5))
###############################
df_ratio_diff = srtdffinal[abs(srtdffinal['Sales Ratio'] - srtdffinal['CalculatedRatio']) > 0.001]
display(df_ratio_diff)
#######################
sales_by_town = df.groupby('Town')['Sale Amount'].sum().sort_values(ascending=False)
display(sales_by_town.head())
#############################
sales_by_town_property = df.groupby(['Town', 'Property Type'])['Sale Amount'].sum().sort_values(ascending=False)
display(sales_by_town_property.head(20))
# Filter for List Year from 2020 to 2022
df_filtered_years = df[(df['List Year'] >= 2020) & (df['List Year'] <= 2022)]

# Group by Town and Property Type, sum Sale Amount, and sort in ascending order
sales_by_town_property_filtered = df_filtered_years.groupby(['Town', 'Property Type','List Year'])['Sale Amount'].sum().sort_values(ascending=True)

display(sales_by_town_property_filtered.head(20))
