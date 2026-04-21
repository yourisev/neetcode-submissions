-- Write your query below

select e.employee_id as employee_id, (CASE 
                                        when e.employee_id % 2 != 0 and e.name not like 'M%' then e.salary
                                        else 0
                                    END) as bonus from employees as e
order by e.employee_id