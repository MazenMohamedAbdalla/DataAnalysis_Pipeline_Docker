import sys
import pandas as pd
import pickle

def call():
  with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
  return loaded_data

def r_dataset(fpath):
    try:
        with open('data.pkl', 'wb') as file:
          data = pd.read_csv(fpath)
          pickle.dump(data, file)
    except FileNotFoundError:
        print(f"File not found: {fpath}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(len(sys.argv))
        print("Usage: python load.py <file_path>")
    else:
        fpath = sys.argv[2]
        r_dataset(fpath)