'''
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference column) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.
 

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.
'''

# Write your MySQL query statement below
with cte_employee as(select e.id, e.name as employee, e.salary, e.departmentid, d.name as department, dense_rank() over(partition by e.departmentid
    order by e.salary desc) as salary_rank
    from employee e
    left join department d on e.departmentid = d.id
    order by salary desc)
select department, employee, salary
from cte_employee
where salary_rank <= 3
order by department;
