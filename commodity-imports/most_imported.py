import pandas as pd

FILE = "data.csv"
DELIMITER = ","

def most_imported():
    '''
    Calculates top 5 commodity imports by various metrics
    '''

    #Read the data
    df = pd.read_csv(FILE, delimiter=DELIMITER)
    cols = df.columns

    print "Top 5 commodities by number of countries imported from"
    print df[cols[0]].value_counts().head()

    print "Top 5 commodities by quantity of import during 2011-2012 and 2012-2013"
    for col in cols[3], cols[5]:
        print df.groupby(cols[0])[[col]].sum().sort([col], ascending=False).head()

    print "Top 5 commodities by cost of import during 2011-2012 and 2012-2013"


if __name__ == "__main__":
    most_imported()
