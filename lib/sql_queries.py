select_all_female_bears_return_name_and_age = """
    SELECT
    bears.name,
    bears.age
FROM bears
WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    Write your SQL query here
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = select_all_alive_bears = """
SELECT
    *
FROM bears
WHERE alive = 1;
"""
select_oldest_bear_and_returns_name_and_age = """
SELECT
    *
FROM bears
ORDER BY age DESC
LIMIT 1;
"""
select_youngest_bear_and_returns_name_and_age = """
SELECT
    *
FROM bears
ORDER BY age ASC
LIMIT 1;
"""