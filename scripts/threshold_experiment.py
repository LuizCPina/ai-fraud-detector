from scripts import analyze_results
from app.ml import generator
from app.services.fraud import engine

THRESHOLD_LIST = [0.3, 0.4, 0.5, 0.6, 0.7]

def run():

    dados = []   

    for _ in range(100):
        transaction = generator.generate_dataset_record()
        record = {
            "transaction": transaction["transaction"],
            "chance": transaction["chance"],
            "fraude": transaction["fraude"],
        }
        dados.append(record)

    

    for threshold in THRESHOLD_LIST:
        resultados = []

        print(f"Running experiment with threshold: {threshold}")

        for record in dados:
            transaction_data = record["transaction"]
            estimativa = engine.analyze_transaction(transaction_data, threshold)

            resultados.append({
                "transaction": record["transaction"],
                "chance": record["chance"],
                "fraude_real": record["fraude"],
                "fraude_estimada": estimativa["fraude_estimada"],
                "risco_estimado": estimativa["risco_estimado"],
                "motivos": estimativa["motivos"]
            })

        analyze_results.run(resultados)

if __name__ == "__main__":
    run()