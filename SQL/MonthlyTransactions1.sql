'''
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
'''

# Write your MySQL query statement below
with cte_transactions as (select id, country, state, amount, date_format(trans_date, '%Y-%m') as month
from transactions) 
select month, country, count(id) as trans_count, sum(case 
        when state = 'approved' then 1
        else 0
    end) as approved_count, sum(amount) as trans_total_amount, sum(case 
        when state = 'approved' then amount
        else 0
    end) as approved_total_amount
from cte_transactions
group by month, country;
