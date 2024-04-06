UPDATE table_name
SET city = REPLACE(city, 'Mayagüez', 'Mayaguez')
WHERE city = 'Mayagüez';
