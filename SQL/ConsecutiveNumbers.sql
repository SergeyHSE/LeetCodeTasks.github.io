'''
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.
'''

# Write your MySQL query statement below
select distinct l1.num as consecutivenums
from logs l1
join logs l2 on l1.id = l2.id-1
join logs l3 on l2.id = l3.id -1
where l1.num = l2.num and l2.num = l3.num;

# Second solution
with temp_table as 
(select id , num , id - dense_rank() over(
    partition by num
    order by id) as rank_number
    from logs
)
select  distinct num as consecutivenums
from temp_table 
group by num, rank_number
having count(rank_number) >=3;
