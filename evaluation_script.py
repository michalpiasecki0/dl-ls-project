import sys

import pandas as pd

import torch
import torch.nn as nn


def load_model(model_path: str) -> nn.Module:
    try:
        return torch.load(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

def evaluate(model: nn.Module, dataset):
    pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python evaluation_script.py <arg1> <arg2>")
        sys.exit(1)

    model_path = sys.argv[1]
    path_test = sys.argv[2]

    model = load_model(model_path)
    data = pd.read_csv(path_test, delimiter='\t')

    evaluate(model, path_test)
    