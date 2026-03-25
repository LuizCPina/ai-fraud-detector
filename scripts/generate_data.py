from app.ml import generator
from app.services.fraud import engine
from app.repositories import transaction_repository

def run():
    for _ in range(1000):
        transaction = generator.generate_dataset_record()
        transaction_data = transaction["transaction"]
        estimativa = engine.analyze_transaction(transaction_data)

        record = {
            "transaction": transaction["transaction"].model_dump(mode="json"),

            "fraude_estimada": estimativa["fraude_estimada"],
            "fraude_real": transaction["fraude"],

            "risco_estimado": estimativa["risco_estimado"],
            "risco_real": transaction["chance"],

            "motivos": estimativa["motivos"]
        }

        transaction_repository.save_transaction(record)

if __name__ == "__main__":
    run()