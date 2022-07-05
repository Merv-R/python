import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Print a Monster registry report.')
    db = pd.read_csv('basic.csv')
    print(db)

main()