# Write your MySQL query statement below
select x,y,z,
case
    when x<0 or y<0 or z<0 then 'No'
    when x+y>z and y+z>x and x+z>y then 'Yes'
    else 'No'
end as triangle
from Triangle