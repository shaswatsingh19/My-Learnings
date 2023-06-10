-- https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations
select 
    EXTRACT(year FROM inspection_date) as year,
    count(violation_id)
from sf_restaurant_health_violations
where business_name = "Roxanne Cafe" AND violation_id IS NOT NULL 
group by year
order by year ;