'''
Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
 

Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column 'name' has unique values.
Table: MovieRating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the users review date. 
 

Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
'''

# Write your MySQL query statement below
with cte_avg_mov as(
    select
        m2.title as title, 
        round(avg(case 
            when created_at like '2020-02%' then rating
            end) over(
                partition by m.movie_id order by m.movie_id), 2) as avg_rats
from movierating m
join movies m2 on m.movie_id = m2.movie_id
join users u on m.user_id = u.user_id
order by avg_rats desc, title
limit 1),
cte_table1 as(select 
    u.name as name,
    row_number() over(
        partition by u.name order by u.name
    ) as num_rats
from movierating m
join movies m2 on m.movie_id = m2.movie_id
join users u on m.user_id = u.user_id
order by num_rats desc, name
limit 1)
select name as results
from cte_table1
union all
select title
from cte_avg_mov;

