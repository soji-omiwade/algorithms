-- write your code in PostgreSQL 9.4
SELECT experience exp, count(*) count, count
(
case when (sql = 100)
and (algo >= 100 )
and (bug_fixing >= 100)
then 1 else 0 end
) max
from assessments 
group by experience
order by experience desc



-- write your code in PostgreSQL 9.4
SELECT experience exp, count(*) count, count
(
case when (sql = 100 OR SQL IS NULL)
and (algo >= 100 or algo is null)
and (bug_fixing >= 100 or bug_fixing is null)
then 1 else 0 end
) max
from assessments 
group by experience
order by experience desc
