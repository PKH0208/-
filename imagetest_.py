# -*- coding: utf-8 -*-
from PIL import Image
import os
import numpy as np
import cv2
import pandas as pd# to_excel()
import tensorflow as tf
import pathlib

# =============================================================================
# def load_and_preprocess_image(file_path):
#     # 이미지 파일을 열고 Pillow를 사용하여 변환
#     img = Image.open(file_path)
#     img = img.convert("RGB")  # RGB 형식으로 변환 (PNG 이미지를 처리하기 위함)
#     img = img.resize((img_height, img_width))  # 이미지 크기 조정
#     img = np.array(img)  # 넘파이 배열로 변환
#     return img
# =============================================================================
# 타입에러 확인해보기
def is_valid_image(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except Exception as e:
        return False

def print_matInfo(name, image):
    # image : 이미지를 읽은 배열값, 이미지데이터
    # image, dtype : 배열요소의 자료형
    if image.dtype == 'uint8' :    mat_type = "CV_8U" # 부호없는 8비트(0~255)
    elif image.dtype == 'int8' :    mat_type = "CV_8S" # 부호있는 8비트(-128~127)
    elif image.dtype == 'uint16' :    mat_type = "CV_16U" # 부호없는 16비트
    elif image.dtype == 'int16' :    mat_type = "CV_16S" # 부호있는 16비트
    elif image.dtype == 'float32' :    mat_type = "CV_32F" # 부호있는 32비트 실수형
    elif image.dtype == 'float64' :    mat_type = "CV_64F" # 부호있는 64비트 실수형
    else : Z.append(file)
    # image.ndim : 배열의 치수
    #nchannel = 3 if image.ndim == 3 else 1
    #print("%12s: dtype(%s),channels(%s) -> mat_type(%sC%d)" % (name,image.dtype,nchannel,mat_type,nchannel))


Z = []
X = []

def process_and_save_images(source_dir):
    invalid_images = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if is_valid_image(file_path):
                    img = load_and_preprocess_image(file_path)
                    X.append(img)
                else:
                    print(f"Invalid image: {file_path}")
                    invalid_images.append(file_path)
                    Z.append(file)
            except:
                Z.append(file_path)
    return invalid_images

source_directory = "C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning/"
invalid_image_list = process_and_save_images(source_directory)
df = pd.DataFrame(Z)
df
df.to_excel('C:/Users/KITCOOP/kicpython/hansik/errorimage.xlsx',index=True)
Z
X
len(Z)
len(X)
# -- excel 불러와서 에러나는 이미지 삭제
import os
import pandas as pd

file_name = 'errorimage.xlsx'
df = pd.read_excel(file_name)
df[0][:-1]
len(df)

cnt=0 # 삭제후 = len(df)
for x in range(len(df)):
    try :
        os.remove(df[0][x])
    except :
        cnt+=1
print(cnt)
os.remove(df[0][1])        

#############

# RGB변환저장하기

from PIL import Image
import os
# 존재하는 폴더
categories = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', 
              '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', 
              '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', 
              '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', 
              '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', 
              '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', 
              '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', 
              '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', 
              '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', 
              '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', 
              '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', 
              '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', 
              '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', 
              '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', 
              '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', 
              '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', 
              '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', 
              '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', 
              '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', 
              '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', 
              '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', 
              '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', 
              '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', 
              '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', 
              '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', 
              '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', 
              '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', 
              '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', 
              '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', 
              '291', '292', '293', '294', '295', '296', '297', '298', '299', '300']
# 폴더내 확장자 추출
directory = "C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning/"
H = []
for category in categories:
    dirc = directory+category+"/"
    for filename in os.listdir(dirc):
        file_extension = os.path.splitext(filename)[-1]
        if file_extension != ".jpg" and file_extension != ".JPG":
            H.append(file_extension)
df = pd.DataFrame(H)    
df.drop_duplicates()    
extension = ['.png','PNG','gif','GIF','jpeg','JPEG','jpg','JPG']


#######이미지 수동으로 전처리
# 훈련 이미지 수정하기 
def modify_and_save_image(cate,cnt):
    exten = ['.jpg','.JPG','.png','.PNG','.gif','.GIF','.jpeg','.JPEG']
    # 파일 경로 설정
    input_directory = "C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning/{category}/"
    # 추출해낸 확장자 선택지에 넣기
    
    # 이미지 파일 열기
    for ex in extension:
       try:
          file_name_in = num + ex
          input_file_path = os.path.join(input_directory, file_name_in)
          img = Image.open(input_file_path)
          break
       except FileNotFoundError:
          print('이미지 파일이 없습니다')
          
    
    print(input_file_path)
    # 이미지를 RGB 색상 모드로 변환
    img = img.convert("RGB")
    # 이미지 수정 
    new_width, new_height = 50, 50
    img = img.resize((new_width, new_height))
    # 수정된 이미지를 새 파일로 저장
    output_directory = "C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning_rgb5/{category}/"
    file_name_out = cnt + ".jpg"
    output_file_path = os.path.join(output_directory, file_name_out)
    img.save(output_file_path)

#변형
for category in categories:
    print("category : ",category)
    data_dir = pathlib.Path("C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning/{category}/")
    os.makedirs("C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning_rgb5/{category}/", exist_ok=True)
    
    # 파일 경로에서 파일 이름을 추출
    file_name = os.path.basename(data_dir)
    last_file_name = os.listdir(data_dir)[-1]
    file_number = last_file_name.split('.')[0]
    image_count = int(file_number)
    print("dic_image 갯수: ",image_count)
    cnt=1
    for _ in range(image_count):
        try:
            if cnt <10 : num = "00"+str(cnt)
            elif cnt >=10 and cnt < 100 : num = "0"+str(cnt)
            else : num = str(cnt)
            modify_and_save_image(category,num)
            cnt += 1    
        except:
            print("이미지 파일이 없습니다","category : ",category,"_",cnt)
            cnt += 1
    print("완료된 image 수 : ",cnt)
############
#test 이미지 수정하기
def modify_and_save_image_test(cate,cnt):
    exten = ['.jpg','.JPG','.png','.PNG','.gif','.GIF','.jpeg','.JPEG']
    # 파일 경로 설정
    input_directory = "C:/Users/KITCOOP/kicpython/hansik/kfood_new/test/"+cate+"/"
    # 추출해낸 확장자 선택지에 넣기
    
    # 이미지 파일 열기
    for ex in exten:
       try:
          file_name_in = num + ex
          input_file_path = os.path.join(input_directory, file_name_in)
          img = Image.open(input_file_path)
          break
       except FileNotFoundError:
          print('이미지파일이 없습니다')
    
    print(input_file_path)
    # 이미지를 RGB 색상 모드로 변환
    img = img.convert("RGB")
    # 이미지 수정 
    new_width, new_height = 50, 50
    img = img.resize((new_width, new_height))
    # 수정된 이미지를 새 파일로 저장
    output_directory = "C:/Users/KITCOOP/kicpython/hansik/kfood_new/test_rgb5/"+cate+"/"
    file_name_out = cnt + ".jpg"
    output_file_path = os.path.join(output_directory, file_name_out)
    img.save(output_file_path)
    

# 변형
for category in categories:
    print("category: ", category)
    input_directory = f"C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning/{category}/"
    os.makedirs(f"C:/Users/KITCOOP/kicpython/hansik/kfood_new/learning_rgb5/{category}/", exist_ok=True)
    
    # 마지막 파일 이름에서 숫자 추출
    last_file_name = os.listdir(input_directory)[-1]
    file_number = int(os.path.splitext(last_file_name)[0])
    
    print("dic_image 갯수: ", file_number)
    for cnt in range(1, file_number + 1):
        modify_and_save_image(category, cnt)
    print("완료된 image 수: ", file_number)

