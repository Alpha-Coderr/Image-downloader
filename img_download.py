import requests
import os
import cv2

def download_image(facetype):
    urls_file=f'urls/{facetype}.txt'
    output_dir=f'images/{facetype}'

    #Creating output directory if it doesnot exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #getting list of urls from text file
    with open(urls_file,'r') as txtfile:
        urls=txtfile.read().strip().split('\n')

    #Dowonload image and save it
    img_num=1
    for url in urls:
        try:
            img_data = requests.get(url).content
            img_path=output_dir+'/'+str(img_num).zfill(8)+'.jpg'
            with open(img_path, 'wb') as img:
                img.write(img_data)
            img_num+=1
            print(f'[Info] Downloaded: {img_path}')
        except:
            print(f'[Info] Error Downloading: {img_path}')

        # Deleting image if opencv cant't open it
        image = cv2.imread(img)
        if image is None:
            print(f'[Info] Image is None! Deleting: {img_path}')
            os.remove(img_path)
