# txt, csv, json, tsv

""" f = open('./data/barack_obama_speech.txt')
lines = f.read().splitlines()
for line in lines:
    print(line.lower().replace('.', ' ').replace(',', ' ').replace(':', ' ').split())
f.close() """

with open('./data/barack_obama_speech.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        print(line.lower().replace('.', ' ').replace(',', ' ').replace(':', ' ').split())
    