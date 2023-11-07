select distinct num ConsecutiveNums
from (
    select num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    from logs
) l
where
num = num1 and num = num2
