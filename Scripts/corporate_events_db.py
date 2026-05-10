import os
from datetime import datetime, date
import psycopg2


#...........PATHS...........#

files_folder = '../Data/Files'


#...........DB CONNECTION...........#

conn = psycopg2.connect(
    host='localhost',
    database='trading',
    user='postgres',
    password='postgres'
)

cur = conn.cursor()


#...........CREATE TABLE...........#

def create_table():

    cur.execute('''

    CREATE TABLE IF NOT EXISTS corporate_events (

        entry_id serial primary key,
        an_bm char(2) CHECK (an_bm IN ('an', 'bm')),
        symbol varchar(30),
        news_date date not null,
        news text

    )

    ''')

    conn.commit()


#...........REMOVE DUPLICATES...........#

def remove_duplicates(parsed_data):

    unique_rows = []

    seen = set()

    for row in parsed_data:

        key = (
            row['an_bm'],
            row['symbol'],
            row['date'],
            row['news']
        )

        if key not in seen:

            seen.add(key)

            unique_rows.append(row)

    return unique_rows


#...........PARSE AN FILE...........#

def parse_an_news_line(line, date):

    line = line.strip()

    if not line:
        return None

    if " : " not in line:
        return None

    left, right = line.split(" : ", 1)

    parts = left.split()

    if len(parts) < 2:
        return None

    symbol = parts[-1]

    company_name = " ".join(parts[:-1])

    return {
        "an_bm": "an",
        "date": date,
        "company_name": company_name,
        "symbol": symbol,
        "news": right.strip()
    }


def read_an_file(filepath, date):

    parsed_an_data = []

    with open(filepath, 'r', encoding='utf-8') as file:

        for line in file:

            data = parse_an_news_line(line, date)

            if data:
                parsed_an_data.append(data)

    parsed_an_data = remove_duplicates(parsed_an_data)

    return parsed_an_data


#...........PARSE BM FILE...........#

def parse_bm_news_line(line, date):

    line = line.strip()

    if not line:
        return None

    if " : " not in line:
        return None

    parts = line.split(" : ")

    if len(parts) < 3:
        return None

    left = parts[0]

    bm_date = parts[1]

    bm_news = " : ".join(parts[2:])

    left_parts = left.split()

    if len(left_parts) < 2:
        return None

    symbol = left_parts[-1]

    company_name = " ".join(left_parts[:-1])

    final_news = f'BM DATE : {bm_date} | {bm_news}'

    return {
        "an_bm": "bm",
        "date": date,
        "company_name": company_name,
        "symbol": symbol,
        "news": final_news
    }


def read_bm_file(filepath, date):

    parsed_bm_data = []

    with open(filepath, 'r', encoding='utf-8') as file:

        for line in file:

            data = parse_bm_news_line(line, date)

            if data:
                parsed_bm_data.append(data)

    parsed_bm_data = remove_duplicates(parsed_bm_data)

    return parsed_bm_data


#...........INSERT INTO DB...........#

def insert_into_db(parsed_data):

    for row in parsed_data:

        cur.execute("""

        INSERT INTO corporate_events
        (an_bm, symbol, news_date, news)

        VALUES (%s, %s, %s, %s)

        """, (

            row['an_bm'],
            row['symbol'],
            row['date'],
            row['news']

        ))

    conn.commit()


#...........GET MAX DATE...........#

def get_max_date():

    cur.execute("""

    SELECT MAX(news_date)
    FROM corporate_events

    """)

    max_date = cur.fetchone()[0]

    return max_date


#...........INITIAL FULL LOAD...........#

def initial_load():

    print('Started Initial Load')

    all_folders = os.listdir(files_folder)

    for folder in all_folders:

        folder_path = os.path.join(
            files_folder,
            folder
        )

        if not os.path.isdir(folder_path):
            continue

        for filename in os.listdir(folder_path):

            filepath = os.path.join(
                folder_path,
                filename
            )

            if not os.path.isfile(filepath):
                continue

            if not filename.endswith('.txt'):
                continue

            if not (
                filename.startswith('an')
                or
                filename.startswith('bm')
            ):
                continue

            date_string = filename[2:10]

            print(date_string, '\n')

            file_date = datetime.strptime(
                date_string,
                "%d%m%Y"
            ).date()

            if filename.startswith('an'):

                parsed_data = read_an_file(
                    filepath,
                    file_date
                )

                insert_into_db(parsed_data)

                print(f'Inserted AN : {filename}')

            elif filename.startswith('bm'):

                parsed_data = read_bm_file(
                    filepath,
                    file_date
                )

                insert_into_db(parsed_data)

                print(f'Inserted BM : {filename}')


#...........RUN...........#

create_table()

max_date = get_max_date()

if max_date is None:

    print('Fresh Database Detected')

    initial_load()

else:

    print(
        f'Database Already Has Data Till : {max_date}'
    )


#...........CLOSE...........#

cur.close()

conn.close()