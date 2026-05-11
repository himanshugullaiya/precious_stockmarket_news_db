import streamlit as st
import pandas as pd
import psycopg2
import pyperclip
import subprocess
import time
from datetime import datetime


#...........PAGE CONFIG...........#

st.set_page_config(
    page_title='Corporate Events Dashboard',
    layout='wide'
)


#...........CUSTOM CSS...........#

st.markdown("""

<style>

h1 {
    font-size: 2.3rem !important;
}

label {
    font-size: 1.05rem !important;
    font-weight: 600 !important;
}

.stTextInput input {
    font-size: 1rem !important;
}

.stDateInput input {
    font-size: 1rem !important;
}

.stMultiSelect div {
    font-size: 1rem !important;
}

button {
    font-size: 1rem !important;
}

</style>

""", unsafe_allow_html=True)


#...........DB CONNECTION...........#

conn = psycopg2.connect(
    host='localhost',
    database='trading',
    user='postgres',
    password='postgres'
)


#...........GET LATEST DATE...........#

def get_latest_date():

    query = """

    SELECT MAX(news_date)
    FROM corporate_events

    """

    df = pd.read_sql(query, conn)

    latest_date = df.iloc[0, 0]

    return latest_date


latest_date = get_latest_date()


#...........TITLE...........#

st.title('Corporate Events Dashboard')


#...........FIRST ROW FILTERS...........#

col1, col2, col3, col4, col5 = st.columns(
    [2, 1, 1, 1, 1]
)


with col1:

    company_search = st.text_input(
        'Company Name'
    )


with col2:

    symbol_search = st.text_input(
        'Symbol'
    )


with col3:

    start_date = st.date_input(
        'Start Date',
        latest_date
    )


with col4:

    end_date = st.date_input(
        'End Date',
        latest_date
    )


with col5:

    an_bm_filter = st.multiselect(
        'Event Type',
        ['an', 'bm'],
        default=['an', 'bm']
    )


#...........SECOND ROW...........#

col6, col7, col8, col9 = st.columns(
    [4, 1, 1, 1]
)


with col6:

    keyword_search = st.text_input(
        'Keywords',
        value='order'
    )


with col7:

    st.write('')
    st.write('')

    search_button = st.button(
        'Search'
    )


with col8:

    st.write('')
    st.write('')

    copy_button = st.button(
        'Copy Symbols'
    )


with col9:

    st.write('')
    st.write('')

    update_button = st.button(
        'Update DB'
    )


#...........BUILD QUERY...........#

query = """

SELECT
    company_name,
    symbol,
    news_date,
    news,
    an_bm

FROM corporate_events

WHERE 1=1

"""

params = []


#...........COMPANY SEARCH...........#

if company_search:

    query += """

    AND company_name ILIKE %s

    """

    params.append(f'%{company_search}%')


#...........SYMBOL SEARCH...........#

if symbol_search:

    query += """

    AND symbol ILIKE %s

    """

    params.append(f'%{symbol_search}%')


#...........DATE FILTER...........#

query += """

AND news_date BETWEEN %s AND %s

"""

params.extend([
    start_date,
    end_date
])


#...........AN BM FILTER...........#

if an_bm_filter:

    placeholders = ','.join(
        ['%s'] * len(an_bm_filter)
    )

    query += f"""

    AND an_bm IN ({placeholders})

    """

    params.extend(an_bm_filter)


#...........KEYWORD FILTER...........#

if keyword_search:

    keywords = [
        x.strip()
        for x in keyword_search.split(',')
        if x.strip()
    ]

    keyword_conditions = []

    for keyword in keywords:

        keyword_conditions.append(
            "news ILIKE %s"
        )

        params.append(f'%{keyword}%')

    query += """

    AND (

    """

    query += " OR ".join(keyword_conditions)

    query += """

    )

    """


#...........FINAL ORDER...........#

query += """

ORDER BY
    news_date DESC,
    symbol

"""


#...........RUN QUERY...........#

df = pd.read_sql(
    query,
    conn,
    params=params
)


#...........COLUMN ORDER...........#

df = df[
    [
        'company_name',
        'symbol',
        'news_date',
        'news',
        'an_bm'
    ]
]


#...........COPY SYMBOLS...........#

if copy_button:

    symbols = sorted(
        df['symbol']
        .dropna()
        .unique()
    )

    symbol_text = ', '.join(symbols)

    pyperclip.copy(symbol_text)

    success_box = st.success(
        'Symbols copied to clipboard'
    )

    time.sleep(3)

    success_box.empty()


#...........UPDATE DATABASE...........#

if update_button:

    update_box = st.info(
        'Updating Database...'
    )

    subprocess.run([
        'python',
        'download_parse_update.py'
    ])

    subprocess.run([
        'python',
        'corporate_events_db.py'
    ])

    update_box.empty()

    success_box = st.success(
        'Database Updated Successfully'
    )

    time.sleep(3)

    success_box.empty()


#...........SHOW COUNTS...........#

st.subheader(
    f'Total Results : {len(df)}'
)


#...........SHOW DATA...........#

st.data_editor(
    df,
    use_container_width=True,
    height=700,
    column_config={

        "company_name": st.column_config.TextColumn(
            "Company Name",
            width="medium"
        ),

        "symbol": st.column_config.TextColumn(
            "Symbol",
            width="small"
        ),

        "news_date": st.column_config.DateColumn(
            "News Date",
            width="small"
        ),

        "news": st.column_config.TextColumn(
            "News",
            width="large"
        ),

        "an_bm": st.column_config.TextColumn(
            "AN/BM",
            width="small"
        )

    },
    disabled=True
)


#...........DOWNLOAD CSV...........#

csv = df.to_csv(index=False)

st.download_button(
    'Download CSV',
    csv,
    file_name='corporate_events.csv',
    mime='text/csv'
)


#...........CLOSE CONNECTION...........#

conn.close()
