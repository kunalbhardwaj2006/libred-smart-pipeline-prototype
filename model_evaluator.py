import time
import json
from typing import List, Dict
from llm_utils import generate_text  # your existing function


MODELS = ["llama3.1", "mistral", "phi3"]


def evaluate_models(prompt: str) -> List[Dict]:
    results = []

    for model in MODELS:
        print(f"\nEvaluating model: {model}")

        start_time = time.time()

        try:
            response = generate_text(prompt, model=model)
            success = True
        except Exception as e:
            response = str(e)
            success = False

        end_time = time.time()

        result = {
            "model": model,
            "success": success,
            "response_time": round(end_time - start_time, 2),
            "response_preview": response[:200] if response else ""
        }

        results.append(result)

    return results


def save_results(results: List[Dict], filename="model_eval_results.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved results to {filename}")


if name == "__main__":
    test_prompt = "Classify this GATE question into subject and subtopic."

    results = evaluate_models(test_prompt)
    save_results(results)
