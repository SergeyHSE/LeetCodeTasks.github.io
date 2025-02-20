'''
Table: Trips
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | varchar  |     
+-------------+----------+
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
 Table: Users
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No').
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.
Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.
'''

# Write your MySQL query statement below
with cte_trips as(select t.id, t.client_id, t.status, t.request_at,
    u.banned
    from trips t
    left join users u on t.client_id = u.users_id
    left join users u2 on t.driver_id = u2.users_id
    where u.banned != 'Yes'
    and u2.banned != 'Yes'
    and request_at between '2013-10-01' and '2013-10-03')
select request_at as day, round(sum(case when status like 'cancelled_by_%' then 1 else 0 end) / count(request_at), 2) as "cancellation rate"
from cte_trips
group by day;
