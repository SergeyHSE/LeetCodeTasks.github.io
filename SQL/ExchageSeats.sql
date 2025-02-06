'''
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
'''

# Write your MySQL query statement below
with cte_seat as (select *, case
    when id % 2 != 0 then id+1
    else id-1
end as new_id
from seat
order by new_id)
select rank() over (order by new_id) as id, student
from cte_seat;
