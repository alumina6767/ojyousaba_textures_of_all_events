import json
import glob

def properties2dic(f, f_path):
    d = {}
    for l in f:
        ll = l.strip(' \n')

        # 空白文字やコメントを読み飛ばす
        if ll == "" or ll[0] == '#':
            continue

        # p=v
        p = ll.split('=')[0].strip(' \n')
        v = ll.split('=')[1].strip(' \n')

        if p == 'items':
            d['item_ids'] = [item_id.replace('minecraft:', '') for item_id in v.split(' ')]

        elif p == 'creators':
            d['creators'] = v.split(' ')

        elif p == 'event':
            d['event'] = v

        elif p == 'category':
            d['category'] = v

        elif p == 'note':
            d['note'] = v

        elif p == 'relation':
            d['relation'] = v

        elif p == 'nbt.display.Name':
            if 'regex' in ll:
                d['name'] = ''.join(ll.split('=')[1:]).encode('ascii').decode('unicode-escape')
            else :
                d['name'] = v.encode().decode('unicode-escape')

        elif p[:3] == 'nbt':
            if 'nbts' not in d:
                d['nbts'] = []

            if 'regex' in ll:
                d['nbts'].append(ll)
            else :
                d['nbts'].append(ll.encode().decode('unicode-escape'))

        # その他の情報
        elif p == 'stackSize' or\
             p == 'enchantments' or\
             p == 'enchantmentLevels' or\
             p == 'damageMask' or\
             p == 'damage' or\
             p == 'hand' or\
             p == 'weight':
             
            if 'etc' not in d:
                d['etc'] = []
            d['etc'].append(ll)

            d[p] = v

        # ファイルパスからサムネイルパスを抽出
        d['image'] = f_path[:-len('properties')].replace('\\','/') + 'mng'

        # コマンドを生成
        #d['command'] = f'give @p {d["item_ids"]}{{{''d["nbts"]}}}'
    return d



if __name__ == '__main__':
    textures = []
    waste_path = len('./assets/minecraft/optifine/cit/')
    for properties in glob.glob('./**/cit/**/*.properties', recursive=True):
        with open(properties,mode='r',encoding='utf-8') as f:
            f_path = properties[waste_path:]
            print(f_path)
            textures.append(properties2dic(f, f_path))

    d = {
        "textures" : textures
    }

    # JSONとして保存
    with open('result.json', mode='w',encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)