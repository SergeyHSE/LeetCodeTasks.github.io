'''
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
 

Write a solution to calculate the bonus of each employee.
The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employees name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.
'''

/* Write your T-SQL query statement below */
select
employee_id,
case 
    when employee_id % 2 != 0 and name not like 'M%' then salary
    else 0
end as bonus
from employees
order by employee_id;
