import numpy as np
import pandas as pd
import csv
import os.path
from os.path import exists

# imports csv as dataframe
df = pd.read_csv("LS_Products.csv")

# changes particular columns of the df into lists
title = list(df["EN_Title_Short"])
sku = list(df["SKU"])
ean = list(df["EAN"])


repeat = True
while repeat == True:
    findEAN = int(input("Enter the EAN of the item you would like to upload:\n> "))
    if findEAN in ean:
        repeat == False
        break
    else:
        print("Item not found")

print(df.loc[ean.index(findEAN), "EN_Title_Short"])
# print(df.loc[sku.index(findEAN)])



# New data formats
titles = []
descShort = []
descLong = []
newSKU = []
newEAN = []
price = []
weight = []
image = []

titles.append(df.loc[ean.index(findEAN), "EN_Title_Short"])
descShort.append(df.loc[ean.index(findEAN), "EN_Description_Short"])
descLong.append(df.loc[ean.index(findEAN), "EN_Description_Long"])
newSKU.append(df.loc[ean.index(findEAN), "SKU"])
newEAN.append(df.loc[ean.index(findEAN), "EAN"])
price.append(df.loc[ean.index(findEAN), "Price"])
weight.append(int(df.loc[ean.index(findEAN), "Weight"])/1000)
image.append(df.loc[ean.index(findEAN), "Images"])


if not os.path.exists('Correctly_Formatted-WP.csv'):
    while True:
        try:
            with open("Correctly_Formatted-WP.csv", 'w', encoding='UTF8', newline='') as f:
                # This creates a csv writer
                writer = csv.writer(f)
                
              

                columnTitles = ["parent_sku","sku", "post_title", "post_excerpt", "post_content", "post_status", "regular_price", "sale_price", "stock_status", "stock", "manage_stock", "weight", "Images", "tax:product_type", "tax:product_cat", "tax:product_tag", "meta:attribute_color", "attribute:color", "attribute_data:color", "attribute_default:color"]
                writer.writerow(columnTitles)  

                #writer.writerow(None)
                print("Correctly_Formatted-WP.csv File Created")
                break
        
        except IOError:
            print("Could not export data! Please close Excel.")


while True:
    try:
        with open("Correctly_Formatted-WP.csv", 'a', encoding='UTF8', newline='') as f:
            # This creates a csv writer
            writer = csv.writer(f)
            
            
            for i in range(len(titles)):
                newRow = ["", newSKU[i], titles[i], descShort[i], descLong[i], "", "", price[i], "", "", "", weight[i], image[i]]
                
                writer.writerow(newRow)  

            #writer.writerow(None)
            
            print("Data Exported")
            
            break
    
    except IOError:
        print("Could not export data! Please close Excel.")
