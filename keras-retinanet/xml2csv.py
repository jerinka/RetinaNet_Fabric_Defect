### xml to csv
import cv2
import os
import pandas as pd
import xml.etree.ElementTree as ET

import csv

def xml2df(xml_path):
    """Convert XML to CSV

    Args:
        xml_path (str): Location of annotated XML file
    Returns:
        pd.DataFrame: converted csv file

    """
    print("xml to csv {}".format(xml_path))
    xml_list = []
    xml_df=pd.DataFrame()
    base = os.path.split(xml_path)[0]
    #import pdb;pdb.set_trace()
    #try:
    if 1:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for member in root.findall('object'):
            #img_nam = os.path.splitext(xml_path)[0]+'.tif'
            head,tail = os.path.split(xml_path)
            head1,tail1 = os.path.split(head)
            
            img_nam = os.path.join(head1,'images',os.path.splitext(tail)[0]+'.tif')
            #print(img_nam)
            #import pdb;pdb.set_trace()
            
            value = (img_nam,
                     #int(root.find('size')[0].text),
                     #int(root.find('size')[1].text),
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text),
                     member[0].text
                     )
            
            xml_list.append(value)
        column_name = ['image_name', 'x_min', 'y_min','x_max','y_max','class_name']
        xml_df = pd.DataFrame(xml_list, columns=column_name)
        
    #except Exception as e:
    #    print('xml conversion failed:{}'.format(e))
    #    return pd.DataFrame(columns=['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'class'])
    return xml_df

def df2csv(df):
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in df.iterrows():
            print(row)
            #print( row['filename'], row['xmin'], row['ymin'], row['xmax'], row['ymax'] , row['class'])
            #writer.writerow([row['filename'], row['xmin'], row['ymin'], row['xmax'], row['ymax'] , row['class']])

def xmls2csv(xml_dir):
    cwd = os.getcwd()
    df = pd.DataFrame()
    for (root,dirs,files) in os.walk(xml_dir, topdown=True):
        
        
        
        appen = root.split(os.sep) [-(len(root.split(os.sep))-len(cwd.split(os.sep))) :]
        
        appen = os.path.join(*appen)
        #print('appen',appen)
        
        for file_ in files:
            if file_.endswith('.xml'):
                file_ = os.path.join(appen, file_)
                print(file_)
                xml_df= xml2df(file_)
                df = df.append(xml_df, ignore_index=True)
             
    return df 

if __name__=='__main__':

    xml_dir = 'maskdb/train/'
    xml_dir=os.path.join(os.getcwd(),xml_dir)
    df = xmls2csv(xml_dir)
    
    df.to_csv('alldata.csv',index=False)#header=False
    print('xml_df',df)
    
    #import pdb;pdb.set_trace()   

    

    

    

