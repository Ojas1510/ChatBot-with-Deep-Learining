import sqlite3
import pandas as pd

timeframes = ['2018-01-01','2019-02-01','2020-01-01','2020-01-02','2020-01-03','2020-01-04','2020-01-05','2020-01-06','2020-01-07',
              '2020-01-08','2020-01-09','2020-01-10']

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False

    while cur_length == limit:

        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection)
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)

        if not test_done:
            with open('test.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+'\n')

            with open('test.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+'\n')

            test_done = True

        else:
            with open('train.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+'\n')

            with open('train.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+'\n')

        counter += 1
        if counter % 20 == 0:
            print(counter*limit,'rows completed so far')
                
            