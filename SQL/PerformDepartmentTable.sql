'''
Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].

Reformat the table such that there is a department id column and a revenue column for each month.
'''

SELECT  id,
    MAX(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,
    MAX(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,
    MAX(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue,
    MAX(CASE WHEN month = 'Apr' THEN revenue END) AS Apr_Revenue,
    MAX(CASE WHEN month = 'May' THEN revenue END) AS May_Revenue,
    MAX(CASE WHEN month = 'Jun' THEN revenue END) AS Jun_Revenue,
    MAX(CASE WHEN month = 'Jul' THEN revenue END) AS Jul_Revenue,
    MAX(CASE WHEN month = 'Aug' THEN revenue END) AS Aug_Revenue,
    MAX(CASE WHEN month = 'Sep' THEN revenue END) AS Sep_Revenue,
    MAX(CASE WHEN month = 'Oct' THEN revenue END) AS Oct_Revenue,
    MAX(CASE WHEN month = 'Nov' THEN revenue END) AS Nov_Revenue,
    MAX(CASE WHEN month = 'Dec' THEN revenue END) AS Dec_Revenue
FROM Department
GROUP BY id;

SELECT id,
    SUM(if(month = 'Jan', revenue, null)) AS Jan_Revenue,
    SUM(if(month = 'Feb', revenue, null)) AS Feb_Revenue,
    SUM(if(month = 'Mar', revenue, null)) AS Mar_Revenue,
    SUM(if(month = 'Apr', revenue, null)) AS Apr_Revenue,
    SUM(if(month = 'May', revenue, null)) AS May_Revenue,
    SUM(if(month = 'Jun', revenue, null)) AS Jun_Revenue,
    SUM(if(month = 'Jul', revenue, null)) AS Jul_Revenue,
    SUM(if(month = 'Aug', revenue, null)) AS Aug_Revenue,
    SUM(if(month = 'Sep', revenue, null)) AS Sep_Revenue,
    SUM(if(month = 'Oct', revenue, null)) AS Oct_Revenue,
    SUM(if(month = 'Nov', revenue, null)) AS Nov_Revenue,
    SUM(if(month = 'Dec', revenue, null)) AS Dec_Revenue
FROM Department
GROUP BY id
