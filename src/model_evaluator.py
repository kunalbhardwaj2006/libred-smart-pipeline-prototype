import time
import random

class ModelEvaluator:
    def __init__(self, models):
        self.models = models

    def simulate_llm_call(self, model_name, question):
        """
        Replace this later with real Ollama call
        """
        start = time.time()

        # Simulated latency
        latency = random.uniform(0.5, 2.5)

        # Simulated accuracy (just for prototype)
        accuracy_score = random.uniform(0.6, 0.9)

        time.sleep(latency)

        return {
            "model": model_name,
            "latency": latency,
            "accuracy": accuracy_score
        }

    def evaluate(self, questions):
        results = {}

        for model in self.models:
            total_latency = 0
            total_accuracy = 0

            for q in questions:
                res = self.simulate_llm_call(model, q)

                total_latency += res["latency"]
                total_accuracy += res["accuracy"]

            results[model] = {
                "avg_latency": total_latency / len(questions),
                "avg_accuracy": total_accuracy / len(questions)
            }

        return results
