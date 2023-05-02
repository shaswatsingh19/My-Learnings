-- https://datalemur.com/questions/tesla-unfinished-parts
SELECT part,assembly_step  FROM parts_assembly
WHERE finish_date IS NULL;