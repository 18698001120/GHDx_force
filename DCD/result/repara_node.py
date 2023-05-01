import csv

if __name__ == '__main__':
    with open('/home/jiangdingyi/jdy/force/result/diseases.csv', 'r') as f:
        with open('/home/jiangdingyi/jdy/force/result/test.txt','w') as w:
            data = csv.DictReader(f)
            for row in data:
                if row['cata'] == '0':
                    # w.write('''{"comments": 0, "connections": 0, "replies": 0, "discussions": 0, "total": '''+row['value']+''', "id": "'''+ row['disease_name'] +''', "color": "#1930FC"},''')
                    w.write('''{"total": '''+row['value']+''', "id": "'''+ row['disease_name'] +'''", "color": "#1930FC"},''')
                elif row['cata'] == '1':
                    w.write('''{"total": '''+row['value']+''', "id": "'''+ row['disease_name'] +'''", "color": "#d62728"},''')
                else:
                    w.write('''{"total": '''+row['value']+''', "id": "'''+ row['disease_name'] +'''", "color": "#00FF00"},''')
        



