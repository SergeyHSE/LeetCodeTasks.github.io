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
WITH first_login AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login_date
    FROM 
        Activity
    GROUP BY 
        player_id
),
next_day_login AS (
    SELECT 
        a.player_id
    FROM 
        Activity a
    JOIN 
        first_login f ON a.player_id = f.player_id 
                   AND a.event_date = DATE_ADD(f.first_login_date, INTERVAL 1 DAY)
)
SELECT 
    ROUND(COUNT(DISTINCT next_day_login.player_id) / COUNT(DISTINCT first_login.player_id), 2) AS fraction
FROM 
    first_login
LEFT JOIN 
    next_day_login ON first_login.player_id = next_day_login.player_id;

;
