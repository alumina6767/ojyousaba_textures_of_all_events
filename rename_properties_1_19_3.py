# 1.19.3用にいろいろ変更する

import glob

optifine_path = ".\\assets\\minecraft\\optifine\\cit"
path_list = glob.glob(optifine_path+'\**\*.properties', recursive=True)

for file_path in path_list:
    with open(file_path, mode='r', encoding='utf_8') as f:
        properties_name = file_path.replace(optifine_path, '').replace(
            '\\', '/').replace('.properties', "")
        new_path = '/'.join(properties_name.split('/')[:-1])+'/'
        new_name = properties_name.split('/')[-1]
        edit_flag = False
        s = f.readlines()

        for i in range(len(s)):
            if "model=" in s[i]:
                s[i] = s[i].replace("model=", "model=item/cit"+new_path)
                edit_flag = True
            elif "texture=" in s[i]:
                s[i] = s[i].replace("texture=", "texture=item/cit"+new_path)
                edit_flag = True
            elif 'texture.' in s[i]:
                s[i] = s[i].replace("=", "=item/cit"+new_path)
                edit_flag = True

        if edit_flag is False:
            # デフォルトでpropertiesのファイル名を使っているtextureを記載する
            s[-1]+='\n'
            s.append("texture=item/cit"+new_path+new_name)
    
    #print(s)
    with open(file_path, mode='w', encoding='utf_8') as f:
        f.writelines(s)
