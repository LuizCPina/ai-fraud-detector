import json

dados = json.load(open("data/transactions.json", "r"))

tp = 0
tn = 0
fp = 0
fn = 0

for record in dados:
    if record["fraude_real"] == True and record["fraude_estimada"] == True:
        tp += 1
    elif record["fraude_real"] == False and record["fraude_estimada"] == False:
        tn += 1
    elif record["fraude_real"] == False and record["fraude_estimada"] == True:
        fp += 1
    elif record["fraude_real"] == True and record["fraude_estimada"] == False:
        fn += 1