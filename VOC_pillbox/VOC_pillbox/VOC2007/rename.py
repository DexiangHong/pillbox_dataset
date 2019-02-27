import glob
import os


root_path = './new_image/'
paths = glob.glob(root_path+'*.jpg')
# print(filenam)
i = 83
for path in paths:
    filename = path.split('\\')[-1]
    # print(filename)
    os.rename(root_path+filename, root_path+str(i)+'.jpg')
    i = i+1
    


