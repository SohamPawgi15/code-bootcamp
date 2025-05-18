-- Weather Observation Station 2
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) 
FROM STATION;

-- Weather Observation Station 3
SELECT DISTINCT CITY 
FROM STATION
WHERE MOD(ID,2) = 0;

-- Employee Names
SELECT name 
from Employee
ORDER BY name;