'''
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places.
In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date,
then divide that number by the total number of players.
'''

# Write your MySQL query statement below
with cte_activity_rank as (select *, dense_rank() over(
    partition by player_id order by event_date
) as date_rank
from activity)
select player_id
from cte_activity_rank 
where event_date in (select date_add(event_date, interval -1 day) as second_date
from cte_activity_rank
where date_rank = 2)
;
