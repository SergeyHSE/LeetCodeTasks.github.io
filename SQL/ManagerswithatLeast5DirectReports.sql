'''
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.
'''
# Write your MySQL query statement below
select e1.name, count(e2.name) as name2, e1.managerid
from employee e1
left join employee e2 on e1.managerid = e2.id
group by e1. name, e1.managerid
having count(e2.name) >= 5;
