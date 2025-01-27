'''
Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
The result format is in the following example.
'''

# first solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    set N = N - 1;
    RETURN (
        select distinct salary
        from employee
        order by salary desc
        limit 1 offset N

    );
END

# second solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        select salary
        from (select salary,
            dense_rank() over(
                order by salary desc) as n_th
        from employee) as salary_number

        where n_th = n
        limit 1
    );
END
