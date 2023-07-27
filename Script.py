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
OriginalStockLevel = list(df["Stock_Level"])
#print(OriginalStockLevel)
#print(len(OriginalStockLevel))


inputOption = input("Would you like to input by EAN or by Category or by SKU? (EAN/Category/SKU):\n> ").lower()
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
                #print(df.loc[ean.index(findEAN), "EN_Title_Short"])
                productTitles.append((df.loc[ean.index(findEAN), "EN_Title_Short"]))
                break
            else:
                print("Item not found")
                

elif inputOption == "sku":

    productSKU = []
    findSKU = "123"
    print("DATA REFORMATER FOR WORDPRESS\nEnter each SKU, then hit ENTER.\n\nWhen all items are entered, submit a 0.\n")
    productTitles = []
    while findSKU != "0":
        repeat = True
        #print(sku)
        while repeat == True:
            findSKU = str(input("Enter the SKU of the item you would like to upload:\n> "))
            if findSKU == "0":
                break
            
            
            elif findSKU in sku:
                repeat == False
                #print(df.loc[ean.index(findEAN), "EN_Title_Short"])
                print((df.loc[sku.index(findSKU), "EN_Title_Short"]))
                productTitles.append((df.loc[sku.index(findSKU), "EN_Title_Short"]))
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
            #print(productTitles)
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
stockLevel = []
dataColour = []
dataSize = []
productType = []

usedMatrixTitles = []

i = 0

print("\n")
print("Import and update these items on WooComerce Products with their matching new SKUs:\n")

for uniqueTitle in productTitles:
#     if np.isnan(uniqueTitle) == False:
    if variant[title.index(uniqueTitle)] == "Default":
        #print(uniqueTitle)

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
        stockLevel.append(df.loc[title.index(uniqueTitle), "Stock_Level"])
        dataColour.append("")
        dataSize.append("")
        productType.append("simple")
    
    elif uniqueTitle not in usedMatrixTitles:

        
        usedMatrixTitles.append(uniqueTitle)
        

        newParentSKU = "PRNT-" + str((df.loc[title.index(uniqueTitle), "SKU"]))[0:3]
        
        
        attribute = (((variant[title.index(uniqueTitle)]).split(" : "))[0])
        
        #print(attribute)
        if "," in attribute.lower() and "color" in attribute.lower() and "size" in attribute.lower():
            #print("TEST")
            #print("ATTRIBUTE:", (attribute.split(","))[0])
            doubleAtt1 = (attribute.split(","))[0]
            #print("ATTRIBUTE:", (attribute.split(","))[1])
            doubleAtt2 = (attribute.split(","))[1]
            attribute = "both"
        colourOptions = []
        sizeOptions = []
        #print(attribute)
        indices = [i for i, x in enumerate(title) if x == uniqueTitle]
        
        

        
        for indice in indices:
            
            # This is where you should append child item info
            #print(((variant[indice]).split(" : "))[1])


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
            stockLevel.append(df.loc[indice, "Stock_Level"])
            dataColour.append("")
            dataSize.append("")
            productType.append("")
            
            if attribute.lower() == "color":
                
                Colour.append("")
                MetaColour.append((variant[indice].split(" : "))[1])
                Size.append("")
                MetaSize.append("")
                
                if int(OriginalStockLevel[indice]) > 0:
                    colourOptions.append((variant[indice].split(" : "))[1])
                #sizeOptions.append("")
                
            elif attribute.lower() == "size":
                Colour.append("")
                MetaColour.append("")
                Size.append("")
                MetaSize.append((variant[indice].split(" : "))[1])
                
                if int(OriginalStockLevel[indice]) > 0:
                    
                    sizeOptions.append((variant[indice].split(" : "))[1])
                #colourOptions.append("")
            
            elif attribute.lower() == "both":
                

                Colour.append("")
                
                doubleAtt1 = (variant[indice]).split(",")[0]
                doubleAtt1 = doubleAtt1.strip('"')
                doubleAtt1 = (doubleAtt1).split(":")[1]
                doubleAtt1 = doubleAtt1.strip(' ')
                #print(doubleAtt1)
                
                MetaColour.append(doubleAtt1)
                #colourOptions.append(doubleAtt1)
                
                Size.append("")
                
                
                doubleAtt2 = (variant[indice]).split(",")[1]
                doubleAtt2 = doubleAtt2.strip('"')
                doubleAtt2 = (doubleAtt2).split(":")[1]
                doubleAtt2 = doubleAtt2.strip(' ')
                #print(doubleAtt2)
                #print(indice, len(OriginalStockLevel))
                #print(OriginalStockLevel[indice])
                
                MetaSize.append(doubleAtt2)
                
                if int(OriginalStockLevel[indice]) > 0:
                    colourOptions.append(doubleAtt1)
                    sizeOptions.append(doubleAtt2)
        
        # This is where you should append parent item info
        print("ITEM:", uniqueTitle, "SKU:", newParentSKU)
        
        parentSKU.append("")
        stockLevel.append("")
        productType.append("variable")
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
        
#         Colour.append("")
#         MetaColour.append("")
#         Size.append("")
#         MetaSize.append("")
#         dataSize.append("")
#         dataColour.append("")
        
        colourAString = "|".join(colourOptions)
        sizeAString = "|".join(sizeOptions)
        #print(colourAString, sizeAString)
        
        #print(len(newSKU), len(newEAN), len(price), len(weight), len(image), len(category1), len(category2), len(category3))

        
        

        #print(attribute.lower())
        if attribute.lower() == "color":
            Colour.append(colourAString)
            MetaColour.append("")
            Size.append("")
            MetaSize.append("")
            dataColour.append("0|1|1")
            dataSize.append("")
            
        elif attribute.lower() == "size":
            Colour.append("")
            MetaColour.append("")
            Size.append(sizeAString)
            MetaSize.append("")
            dataSize.append("0|1|1")
            dataColour.append("")
            
        elif attribute.lower() == "both":
    
            Colour.append(colourAString)
            MetaColour.append("")
            Size.append(sizeAString)
            MetaSize.append("")
            dataColour.append("0|1|1")
            dataSize.append("0|1|1")
            
        
        
        
            
    
    i += 1
    
    #print("NEW", len(Colour), len(MetaColour), len(Size), len(MetaSize), len(dataColour), len(dataSize))
    




if not os.path.exists('Correctly_Formatted_WP.csv'):
    while True:
        try:
            with open("Correctly_Formatted_WP.csv", 'w', encoding='UTF8', newline='') as f:
                # This creates a csv writer
                writer = csv.writer(f)
                
              

                columnTitles = ["parent_sku","sku", "post_title", "post_excerpt", "post_content", "post_status", "regular_price", "sale_price", "stock_status", "stock", "manage_stock", "weight", "Images", "tax:product_type", "tax:product_cat", "tax:product_tag", "meta:attribute_Color", "attribute:Color", "attribute_data:Color", "attribute_default:Color", "meta:attribute_Size", "attribute:Size", "attribute_data:Size"]
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
                if "PRNT" in str(newSKU[i]): 
                    newRow = [parentSKU[i], newSKU[i], titles[i], descShort[i], descLong[i], "publish", price[i], (price[i] * .8), "instock", "", "", weight[i], image[i], productType[i], productCategory, "", MetaColour[i], Colour[i], dataColour[i], "", MetaSize[i], Size[i], dataSize[i]]
                    writer.writerow(newRow)                

                elif stockLevel[i] == "": 
                    newRow = [parentSKU[i], newSKU[i], titles[i], descShort[i], descLong[i], "draft", price[i], (price[i] * .77), "instock", "", "", weight[i], image[i], productType[i], productCategory, "", MetaColour[i], Colour[i], dataColour[i], "", MetaSize[i], Size[i], dataSize[i]]
                    writer.writerow(newRow)
                    
                elif int(stockLevel[i]) > 0:
                    newRow = [parentSKU[i], newSKU[i], titles[i], descShort[i], descLong[i], "publish", price[i], (price[i] * .77), "instock", "", "", weight[i], image[i], productType[i], productCategory, "", MetaColour[i], Colour[i], dataColour[i], "", MetaSize[i], Size[i], dataSize[i]]
                    writer.writerow(newRow)
                
                else:
                    newRow = [parentSKU[i], newSKU[i], titles[i], descShort[i], descLong[i], "draft", price[i], (price[i] * .77), "instock", "", "", weight[i], image[i], productType[i], productCategory, "", MetaColour[i], Colour[i], dataColour[i], "", MetaSize[i], Size[i], dataSize[i]]
                    writer.writerow(newRow)

            #writer.writerow(None)
            
            print("Data Exported")
            
            break
    
    except IOError:
        print("Could not export data! Please close Excel.")
