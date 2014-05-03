import pandas as pd

FILE = "data.csv"
DELIMITER = ","

def most_imported():
    '''
    Calculates top commodity imports by various metrics
    '''

    #Read the data
    df = pd.read_csv(FILE, delimiter=DELIMITER)

    #Top 5 commodities by number of countries imported from
    print df[df.columns[0]].value_counts().head()


if __name__ == "__main__":
    most_imported()
