'''
able: Stadium

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the column with unique values for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
As the id increases, the date increases as well.
 

Write a solution to display the records with three or more rows with consecutive ids, and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.
'''

# Write your MySQL query statement below
with cte_bull as (select id, visit_date, people, case when people >= 100 then 1 else 0 end as bull
from stadium),
cte_sum as (select *, sum(bull) over(order by id) as sum_bull
from cte_bull
where bull = 1),
cte_unique as (select *, id - sum_bull as uniques
from cte_sum),
cte_end as (select *, count(uniques) over(partition by uniques) as count_uniq
from cte_unique)
select id, visit_date, people
from cte_end
where count_uniq > 2
order by id;
