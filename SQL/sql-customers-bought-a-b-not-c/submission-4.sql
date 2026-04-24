-- Write your query below
select distinct b_customer_id as customer_id, customer_name from customers
join (select distinct *  from (select distinct order_id as b_order_id, customer_id as b_customer_id, product_name as b_product_name from orders as b_orders 
                join (select distinct order_id as a_order_id, customer_id as a_customer_id, product_name as a_product_name from orders
                        where product_name = 'A'
                        ) as a_orders 
                on b_orders.customer_id = a_orders.a_customer_id
                where b_orders.product_name = 'B'
                ) as ab_orders
left join ( select distinct * from orders as not_c_orders
                where product_name = 'C') as c_orders
on customer_id = b_customer_id
where product_name is null) as expected_orders
on customers.customer_id = expected_orders.b_customer_id
order by customer_name