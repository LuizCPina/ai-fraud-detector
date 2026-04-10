import json

dados = json.load(open("data/transactions.json", "r"))

def run (dados):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for record in dados:
        if record["fraude_real"] and record["fraude_estimada"]:
            tp += 1
        elif not record["fraude_real"] and not record["fraude_estimada"]:
            tn += 1
        elif not record["fraude_real"] and record["fraude_estimada"]:
            fp += 1
        elif record["fraude_real"] and not record["fraude_estimada"]:
            fn += 1


    total = tp + tn + fp + fn
    accuracy = (tp + tn) / total if total > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    print(f"True Positives: {tp}")
    print(f"True Negatives: {tn}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    run(dados)