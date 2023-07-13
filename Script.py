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
categories = list(df["EN_Category_1"])
categories2 = list(df["EN_Category_2"])
categories3 = list(df["EN_Category_3"])
variant = list(df["EN_Variant"])



inputOption = input("Would you like to input by EAN or by Category? (EAN/Category):\n> ").lower()
if inputOption == "ean":

    productEANS = []
    findEAN = 123
    print("DATA REFORMATER FOR WORDPRESS\nEnter each EAN, then hit ENTER.\n\nWhen all items are entered, submit a 0.\n")
    productTitles = []
    while findEAN != 0:
        repeat = True
        while repeat == True:
            findEAN = int(input("Enter the EAN of the item you would like to upload:\n> "))
            if findEAN == 0:
                break
            
            elif findEAN in ean:
                repeat == False
                print(df.loc[ean.index(findEAN), "EN_Title_Short"])
                productTitles.append((df.loc[ean.index(findEAN), "EN_Title_Short"]))
                break
            else:
                print("Item not found")
                
                
elif inputOption == "category":
    repeat = True
    while repeat == True:
        findCategory = (input("Enter the CATEGORY of the items you would like to upload:\n> "))
        if findCategory in categories or findCategory in categories2 or findCategory in categories3:
            i=0
            productTitles = []
            for category in categories:
                if category == findCategory:
#                     if productTitles.append(df.loc[i, "EN_Title_Short"]) != None:
                    productTitles.append((df.loc[i, "EN_Title_Short"]))
                i+=1
                        
            i=0
            for category in categories2:
                if category == findCategory:
#                     if productTitles.append(df.loc[i, "EN_Title_Short"]) != None:
                    productTitles.append((df.loc[i, "EN_Title_Short"]))
                i+=1
            i=0
            for category in categories3:
                if category == findCategory:
#                     if productTitles.append(df.loc[i, "EN_Title_Short"]) != None:
                    productTitles.append((df.loc[i, "EN_Title_Short"]))
                i+=1
            print(productTitles)
            repeat == False
            break
        else:
            print("Item not found")
        





# New data formats
titles = []
descShort = []
descLong = []
newSKU = []
newEAN = []
price = []
weight = []
image = []
category1 = []
category2 = []
category3 = []
Colour = []
MetaColour = []
Size = []
MetaSize = []
parentSKU = []


usedMatrixTitles = []

i = 0



for uniqueTitle in productTitles:
#     if np.isnan(uniqueTitle) == False:
    if variant[title.index(uniqueTitle)] == "Default":
        print(uniqueTitle)

        titles.append(df.loc[title.index(uniqueTitle), "EN_Title_Short"])
        descShort.append(df.loc[title.index(uniqueTitle), "EN_Description_Short"])
        descLong.append(df.loc[title.index(uniqueTitle), "EN_Description_Long"])
        newSKU.append(df.loc[title.index(uniqueTitle), "SKU"])
        newEAN.append(df.loc[title.index(uniqueTitle), "EAN"])
        price.append(df.loc[title.index(uniqueTitle), "Price"])
        weight.append(int(df.loc[title.index(uniqueTitle), "Weight"])/1000)
        image.append(df.loc[title.index(uniqueTitle), "Images"])
        category1.append(df.loc[title.index(uniqueTitle), "EN_Category_1"])
        category2.append(df.loc[title.index(uniqueTitle), "EN_Category_2"])
        category3.append(df.loc[title.index(uniqueTitle), "EN_Category_3"])
        Colour.append("")
        MetaColour.append("")
        Size.append("")
        MetaSize.append("")
        parentSKU.append("")
    
    elif uniqueTitle not in usedMatrixTitles:

        
        usedMatrixTitles.append(uniqueTitle)
        

        newParentSKU = "PRNT-" + (df.loc[title.index(uniqueTitle), "SKU"])[0:3]
        print(newParentSKU)
        
        attribute = (((variant[title.index(uniqueTitle)]).split(" : "))[0])
        colourOptions = []
        sizeOptions = []
        print(attribute)
        indices = [i for i, x in enumerate(title) if x == uniqueTitle]
        
        
        for indice in indices:
            
            # This is where you should append child item info
            print(((variant[indice]).split(" : "))[1])


            titles.append("")
            descShort.append("")
            descLong.append("")
            image.append("")
            category1.append(df.loc[title.index(uniqueTitle), "EN_Category_1"])
            category2.append(df.loc[title.index(uniqueTitle), "EN_Category_2"])
            category3.append(df.loc[title.index(uniqueTitle), "EN_Category_3"])   
            newSKU.append(df.loc[indice, "SKU"])
            newEAN.append(df.loc[indice, "EAN"])
            price.append(df.loc[indice, "Price"])
            weight.append(int(df.loc[indice, "Weight"])/1000)
            parentSKU.append(newParentSKU)
            
            if attribute.lower() == "color":
                
                Colour.append("")
                MetaColour.append((variant[indice].split(" : "))[1])
                Size.append("")
                MetaSize.append("")
                colourOptions.append((variant[indice].split(" : "))[1])
                
            elif attribute.lower() == "size":
                Colour.append("")
                MetaColour.append("")
                Size.append("")
                MetaSize.append((variant[indice].split(" : "))[1])
                sizeOptions.append((variant[indice].split(" : "))[1])
        
        # This is where you should append parent item info
        print("MATRIX:", uniqueTitle)
        
        parentSKU.append("")
        
        titles.append(df.loc[title.index(uniqueTitle), "EN_Title_Short"])
        descShort.append(df.loc[title.index(uniqueTitle), "EN_Description_Short"])
        descLong.append(df.loc[title.index(uniqueTitle), "EN_Description_Long"])
        newSKU.append(newParentSKU)
        newEAN.append(df.loc[title.index(uniqueTitle), "EAN"])
        price.append(df.loc[title.index(uniqueTitle), "Price"])
        weight.append(int(df.loc[title.index(uniqueTitle), "Weight"])/1000)
        image.append(df.loc[title.index(uniqueTitle), "Images"])
        category1.append(df.loc[title.index(uniqueTitle), "EN_Category_1"])
        category2.append(df.loc[title.index(uniqueTitle), "EN_Category_2"])
        category3.append(df.loc[title.index(uniqueTitle), "EN_Category_3"])
        
        colourAString = "|".join(colourOptions)
        sizeAString = "|".join(sizeOptions)

        
        if attribute.lower() == "color":
            Colour.append(colourAString)
            MetaColour.append("")
            Size.append("")
            MetaSize.append("")
            
        elif attribute.lower() == "size":
            Colour.append("")
            MetaColour.append("")
            Size.append(sizeAString)
            MetaSize.append("")
        
            
    
    i += 1
    
    




if not os.path.exists('Correctly_Formatted_WP.csv'):
    while True:
        try:
            with open("Correctly_Formatted_WP.csv", 'w', encoding='UTF8', newline='') as f:
                # This creates a csv writer
                writer = csv.writer(f)
                
              

                columnTitles = ["parent_sku","sku", "post_title", "post_excerpt", "post_content", "post_status", "regular_price", "sale_price", "stock_status", "stock", "manage_stock", "weight", "Images", "tax:product_type", "tax:product_cat", "tax:product_tag", "meta:attribute_color", "attribute:color", "attribute_data:color", "attribute_default:color", "meta:attribute_size", "attribute:size"]
                writer.writerow(columnTitles)  

                #writer.writerow(None)
                print("Correctly_Formatted_WP.csv.csv File Created")
                break
        
        except IOError:
            print("Could not export data! Please close Excel.")


while True:
    try:
        with open("Correctly_Formatted_WP.csv", 'a', encoding='UTF8', newline='') as f:
            # This creates a csv writer
            writer = csv.writer(f)
            
            
            
            for i in range(len(titles)):
                productCategory = str(category1[i])

                if str(category2[i]) != "nan":
                    productCategory = productCategory +"|"+ str(category2[i])
                    if str(category3[i]) != "nan":
                        productCategory = productCategory +"|"+ str(category3[i])
                newRow = [parentSKU[i], newSKU[i], titles[i], descShort[i], descLong[i], "", price[i], "", "", "", "", weight[i], image[i], "", productCategory, "", MetaColour[i], Colour[i], "", "", MetaSize[i], Size[i]]
                
                writer.writerow(newRow)  

            #writer.writerow(None)
            
            print("Data Exported")
            
            break
    
    except IOError:
        print("Could not export data! Please close Excel.")
