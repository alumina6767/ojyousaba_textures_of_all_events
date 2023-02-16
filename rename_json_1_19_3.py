# 1.19.3用にいろいろ変更する

import glob

optifine_path = ".\\assets\\minecraft\\models\\item\\cit"
path_list = glob.glob(optifine_path+'\**\*.json', recursive=True)

for file_path in path_list:
    with open(file_path, mode='r', encoding='utf_8') as f:
        properties_name = file_path.replace(optifine_path, '').replace(
            '\\', '/').replace('.properties', "")
        new_path = '/'.join(properties_name.split('/')[:-1])+'/'
        new_name = properties_name.split('/')[-1]
        edit_flag = False
        s = f.read()
        s = s.replace('./', 'item/cit'+new_path)

    with open(file_path, mode='w', encoding='utf_8') as f:
         f.write(s)
