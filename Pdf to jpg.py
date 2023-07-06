import requests
import os
import fitz
import io
from PIL import Image

#Mention the Id for a particular Pdf inside an array
array = ['5ff8902f-0568-4c57-86b0-f6aaa0e1a0b9','36289228-85fc-4346-af0a-d1aadcde10d3','da2eb3d0-c01a-46a7-a91b-6214da9db6e3','936efee8-7c76-4233-92db-3f7d0d9b2e0c',
         '8afde3cd-221d-4336-a6be-48e92bcf4b74']

trimmed_array = []

#Framing the URL
for item in array:
    path = os.path.join("D:/pdf/", item) #Path for saving the cropped images in their respective folders. 
    os.makedirs(path, exist_ok=True)
    photourl = 'https://sgbimages.s3.ap-south-1.amazonaws.com/'+item+'/UserPhoto_.pdf'
    signUrl = 'https://sgbimages.s3.ap-south-1.amazonaws.com/'+item+'/UserSignature_.pdf'
    
    #Downloading the Pdf
    response = requests.get(photourl, stream = True)
    if response.status_code == 200:
        filepath = os.path.join(path,'UserPhoto_.pdf')
        
        with open(filepath, 'wb') as pdf_object:
            pdf_object.write(response.content)
            
        pdf_file = fitz.open(filepath)

        for page_index in range(len(pdf_file)):

            # get the page itself
            page = pdf_file[page_index]
            image_list = page.get_images()

            # printing number of images found in this page
            if image_list:
                print(
                    f"[+] Found a total of {len(image_list)} images in page {page_index}")
            else:
                print("[!] No images found on page", page_index)
            for image_index, img in enumerate(page.get_images(), start=1):
                # get the XREF of the image
                xref = img[0]

                # extract the image bytes
                base_image = pdf_file.extract_image(xref)
                image_bytes = base_image["image"]

                # get the image extension
                image_ext = base_image["ext"]
                imagepath = os.path.join(path,'UserPhoto_.'+image_ext)
                        # Save image
                with open(imagepath, 'wb') as image_file:
                    image_file.write(image_bytes)
                    image_file.close()

            ###
        
    
    response = requests.get(signUrl, stream = True)
    if response.status_code == 200:
        filepath = os.path.join(path,'UserSignature_.pdf')
        with open(filepath, 'wb') as pdf_object:
            pdf_object.write(response.content)    
        
        pdf_file = fitz.open(filepath)

        for page_index in range(len(pdf_file)):

            # get the page itself
            page = pdf_file[page_index]
            image_list = page.get_images()

            # printing number of images found in this page
            if image_list:
                print(
                    f"[+] Found a total of {len(image_list)} images in page {page_index}")
            else:
                print("[!] No images found on page", page_index)
            for image_index, img in enumerate(page.get_images(), start=1):
                # get the XREF of the image
                xref = img[0]

                # extract the image bytes
                base_image = pdf_file.extract_image(xref)
                image_bytes = base_image["image"]

                # get the image extension
                image_ext = base_image["ext"]
                imagepath = os.path.join(path,'UserSignature_.'+image_ext)
                        # Save image
                with open(imagepath, 'wb') as image_file:
                    image_file.write(image_bytes)
                    image_file.close()

            
            
