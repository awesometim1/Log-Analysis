#!/usr/bin/python3
import datetime
import psycopg2


def top3_articles():
    """Connect to the database news and perform a query that
    returns the top 3 articles"""
    query = '''
    select title, views from articles,
    (select path, count(path) as views from log
    group by log.path) as log
    where '/article/' || articles.slug = log.path
    order by views desc
    limit 3;'''
    posts = execute_query(query)
    print("Top 3 Articles by Views ~ \n")
    for title, views in posts:
        print('"{}" - {} views'.format(title, views))
    print("\n")


def author_ranking():
    """Connect to the database news and perform a query that
    returns the authors rankings"""
    query = '''
    select name, sum(views) as num from articles, authors,
    (select path, count(path) as views from log
    group by log.path) as log
    where '/article/' || articles.slug = log.path
    and articles.author = authors.id
    group by name
    order by num desc;'''
    posts = execute_query(query)
    print("Author Rank by Article Views ~ \n")
    for author, views in posts:
        print('"{}" - {} views'.format(author, views))
    print("\n")


def error_dates():
    """Connect to the database news and perform a query that
    returns dates that have more than 1% error rate while trying to access
    the webpage."""
    query = '''select * from
    (select to_char(date,'FMMonth, DD YYYY'),
    (four::decimal/two) as perc
    from(select time::date as date ,
    sum(case when status like '%404%' then 1 end) as four,
    count(*) as two
    from log
    group by date) as comp
    order by perc desc) as ma
    where ma.perc > .01
    ;'''
    posts = execute_query(query)
    print("Dates with more than 1% error rate ~ \n")
    for date, err in posts:
        print('{} - {:.2%} errors'.format(date, err))
    print("\n")


def execute_query(query):
    try:
        conn = psycopg2.connect("dbname=news")
        c = conn.cursor()
        c.execute(query)
        result = c.fetchall()
        conn.close()
        return result
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    top3_articles()
    author_ranking()
    error_dates()
