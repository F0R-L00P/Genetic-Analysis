from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from functools import reduce

# =============================================================================
# Parser Function
# =============================================================================
def gene_parser(url):
    # access page read data from web
    page = urllib.request.urlopen(url).read()
    # save data in soup object
    soup = BeautifulSoup(page)
    # extract body and save in object
    body = soup.find('body')
    
    # extract body string and save in list
    html_strings = []
    for i in body.strings:
        html_strings.append(i)
    
    # access 5th element of list where table is residing
    # seperate data at end of each sentence
    temp = html_strings[5].split('\n')
    
    # extract all table values
    # split at space between values
    raw_data = []
    for i in range(len(temp)):
        raw_data.append(temp[i].split('\t'))
    
    # build first df, both values are in single cell
    df_aggregate = pd.DataFrame({'value': raw_data})
    
    # split column 
    df = pd.DataFrame({})
    df[['gene', 'p_value']] = pd.DataFrame(df_aggregate['value'].values.tolist())
    
    # drop empty rows
    df = df.dropna(axis=0)
    # replace string with int, convert column to float    
    df['p_value'].replace('null', 0, inplace=True)      
    df['p_value'] = pd.to_numeric(df['p_value'])    
    
    return df

# =============================================================================
# Control 1_white matter tissue
# =============================================================================
url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886523&id=46221&db=GeoDb_blob158'
df1 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886524&id=46222&db=GeoDb_blob158'
df2 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886525&id=46223&db=GeoDb_blob158'
df3 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886526&id=46224&db=GeoDb_blob158'
df4 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886527&id=46225&db=GeoDb_blob158'
df5 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886528&id=46226&db=GeoDb_blob158'
df6 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886529&id=46227&db=GeoDb_blob158'
df7 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886530&id=46228&db=GeoDb_blob158'
df8 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886531&id=46229&db=GeoDb_blob158'
df9 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886532&id=46230&db=GeoDb_blob158'
df10 = gene_parser(url)

# =============================================================================
# RIM Chronic active MS lesion
# =============================================================================
url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886533&id=46231&db=GeoDb_blob158'
df11 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886534&id=46232&db=GeoDb_blob158'
df12 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886535&id=46233&db=GeoDb_blob158'
df13 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886536&id=46234&db=GeoDb_blob158'
df14 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886537&id=46235&db=GeoDb_blob158'
df15 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886538&id=46236&db=GeoDb_blob158'
df16 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886539&id=46237&db=GeoDb_blob158'
df17 = gene_parser(url)
# =============================================================================
# Perilesion Chronic active MS lesion
# =============================================================================
url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886540&id=46238&db=GeoDb_blob158'
df18 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886541&id=46239&db=GeoDb_blob158'
df19 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886542&id=46240&db=GeoDb_blob158'
df20 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886543&id=46241&db=GeoDb_blob158'
df21 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886544&id=46242&db=GeoDb_blob158'
df22 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886545&id=46243&db=GeoDb_blob158'
df23 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886546&id=46244&db=GeoDb_blob158'
df24 = gene_parser(url)
# =============================================================================
# RIM Inactive MS lesion
# =============================================================================
url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886547&id=46245&db=GeoDb_blob158'
df25 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886548&id=46246&db=GeoDb_blob158'
df26 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886549&id=46247&db=GeoDb_blob158'
df27 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886550&id=46248&db=GeoDb_blob158'
df28 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886551&id=46249&db=GeoDb_blob158'
df29 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886552&id=46250&db=GeoDb_blob158'
df30 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886553&id=46251&db=GeoDb_blob158'
df31 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886554&id=46252&db=GeoDb_blob158'
df32 = gene_parser(url)
# =============================================================================
# Perilesion Inactive MS lesion
# =============================================================================
url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886555&id=46253&db=GeoDb_blob158'
df33 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886556&id=46254&db=GeoDb_blob158'
df34 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886557&id=46255&db=GeoDb_blob158'
df35 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886558&id=46256&db=GeoDb_blob158'
df36 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886559&id=46257&db=GeoDb_blob158'
df37 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886560&id=46258&db=GeoDb_blob158'
df38 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886561&id=46259&db=GeoDb_blob158'
df39 = gene_parser(url)

url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886562&id=46260&db=GeoDb_blob158'
df40 = gene_parser(url)

# =============================================================================
# Merge Data and Change Column Header
# =============================================================================
dfs = [df1, df2, df3, df4, df5, 
       df6, df7, df8, df9, df10, 
       df11, df12, df13, df14, df15, 
       df16, df17, df18, df19, df20, 
       df21, df22, df23, df24, df25, 
       df26, df27, df28, df29, df30, 
       df31, df32, df33, df34, df35, 
       df36, df37, df38, df39, df40]

# merge multiple data using reduce function
merge_data = reduce(lambda x, y: pd.merge(x, y, on='gene', how='left'), dfs)

# change column headers to match data samples from ncbi
merge_data.columns = ['gene', 
                      'control1_wmt', 'control2_wmt', 
                      'control3_wmt', 'control4_wmt', 
                      'control5_wmt', 'control6_wmt', 
                      'control7_wmt', 'control8_wmt', 
                      'control9_wmt', 'control10_wmt',
                      'rim_active1', 'rim_active2', 'rim_active3', 
                      'rim_active4', 'rim_active5', 'rim_active6', 'rim_active7', 
                      'perilesion_active1', 'perilesion_active2', 'perilesion_active3', 
                      'perilesion_active4', 'perilesion_active5', 'perilesion_active6', 'perilesion_active7',
                      'rim_inactive1', 'rim_inactive2', 'rim_inactive3', 'rim_inactive4', 
                      'rim_inactive5', 'rim_inactive6', 'rim_inactive7', 'rim_inactive8', 
                      'perilesion_inactive1', 'perilesion_inactive2', 'perilesion_inactive3', 
                      'perilesion_inactive4', 'perilesion_inactive5', 'perilesion_inactive6', 
                      'perilesion_inactive7', 'perilesion_inactive8']

# =============================================================================
# Write file to csv
# =============================================================================
merge_data.to_csv('gene_dataset.csv', index = False)