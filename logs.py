#!/usr/bin/env python

import psycopg2

DBNAME = "news"

query1 = """SELECT title, count(*) as views \n
            FROM articles JOIN log on \n
            CONCAT('/article/', articles.slug) = log.path \n
            GROUP BY title ORDER BY views DESC LIMIT 3;"""

query2 = """SELECT authors.name, count(*) as views \n
            FROM articles,authors,log \n
            WHERE articles.author = authors.id \n
            AND CONCAT('/article/', articles.slug) = log.path \n
            GROUP BY authors.name ORDER BY views DESC;"""

query3 = """SELECT date(time), round(100.0*sum(CASE log.status \n
            WHEN '404 NOT FOUND' THEN 1 \n
            ELSE 0 \n
            END \n)/count(log.status), 2) as total_error \n
            FROM log \n
            GROUP BY date(time) ORDER BY total_error DESC LIMIT 1;"""

#To connect to DB and run query:

def get_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

result1 = get_query(query1)
result2 = get_query(query2)
result3 = get_query(query3)

#To print the results stored:

def print_res(results):
    for i in range(len(results)):
        ar_name = results[i][0]
        ar_clicks = results[i][1]
        print("\t" + "%s" % (ar_name) + " - " + "%d" %(ar_clicks) + " views")
    print("\n")

print("What are the most popular articles of all time?")
print_res(result1)
print("What are the most popular article authors of all time?")
print_res(result2)
print("On which days more than 1% of requests lead to error?")
print("\t" + str(result3[0][0]) + " - " + str(result3[0][1]) + "%")
