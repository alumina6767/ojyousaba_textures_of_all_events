# テクスチャしか置き換えられていないCITにモデルをつける

import glob
import json

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
            if "texture=" in s[i]:
                texture = s[i].replace("texture=","").replace(".png","").strip()
                s[i] = s[i].replace("texture=", "model=").replace(".png","")
                edit_flag = True

    if edit_flag is True:
        # .propertiesの書き換え
        with open(file_path, mode='w', encoding='utf_8') as f:
            f.writelines(s)

        # JSONモデルの追加
        model_file_path = file_path.replace('minecraft\\optifine\\','minecraft\\models\\item\\').replace('.properties','.json')
        with open(model_file_path, mode='w', encoding='utf_8') as f:
            d = { 
                    "parent" : "minecraft:item/generated",
                    "textures": 
                        {"layer0": texture}
                }
            json.dump(d, f, indent=4)

