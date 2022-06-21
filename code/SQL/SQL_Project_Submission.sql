-- SQL Text File for Project Submission

-- Set #1 Question 1
/*
We want to understand more about the movies that families are watching. 
The following categories are considered family movies: Animation, Children,
Classics, Comedy, Family and Music.

Create a query that lists each movie, the film category it is classified in,
and the number of times it has been rented out. 
*/

WITH movies_and_rentals AS (
	SELECT a.film_id
		, a.title AS film_title
		--, a.description
		, c.name AS category_name
		, d.inventory_id
		, e.rental_id
		, e.rental_date
	FROM film a
	INNER JOIN film_category b
		ON a.film_id = b.film_id
	INNER JOIN category c
		ON b.category_id = c.category_id
	INNER JOIN inventory d
		ON a.film_id = d.film_id
	INNER JOIN rental e
		ON d.inventory_id = e.inventory_id
	WHERE c.name IN ('Animation','Children','Classics','Family','Comedy', 'Music')
)

SELECT film_title
	, category_name
    , COUNT(rental_id) AS rental_count
FROM movies_and_rentals
GROUP BY 1, 2
ORDER BY 3 DESC
;

-- Set #1 Question 2
/*
Now we need to know how the length of rental duration of these family-
friendly movies compares to the duration that all movies are rented for.
Can you provide a table with the movie titles and divide them into 4 
levels (first_quarter, second_quarter, third_quarter, and final_quarter) 
based on the quartiles (25%, 50%, 75%) of the rental duration for movies 
across all categories? Make sure to also indicate the category that these 
family-friendly movies fall into.
*/

WITH duration_cte AS (
	SELECT rental_id
		, inventory_id
		, DATE_PART('day',return_date - rental_date) AS rental_duration
		-- finding duration of each rental for all categories
	FROM rental
	WHERE rental_date IS NOT NULL
		AND return_date IS NOT NULL
)

, movie_rental_durations AS (
	SELECT b.film_id
		-- , a.rental_id
		, c.title AS film_title
		, AVG(a.rental_duration) AS avg_rental_duration_per_movie
	FROM duration_cte a
	INNER JOIN inventory b
		ON b.inventory_id = a.inventory_id
	INNER JOIN film c
		ON c.film_id = b.film_id
	GROUP BY 1,2
)

, quartiles_cte AS (
	SELECT film_title
		, a.film_id
		, c.name AS category_name
		-- , inventory_id
		, avg_rental_duration_per_movie
		, NTILE(4) OVER (ORDER BY avg_rental_duration_per_movie) AS quartile
		-- grouping each rental into a quartile for rental duration
	FROM movie_rental_durations a
	INNER JOIN film_category b
		ON a.film_id = b.film_id
	INNER JOIN category c
		ON b.category_id = c.category_id
)

SELECT * FROM quartiles_cte
WHERE category_name IN ('Animation',
	'Children',
	'Classics',
	'Family',
	'Comedy',
	'Music')
;

-- Set #1 Question 3
/*
Finally, provide a table with the family-friendly film category, each
of the quartiles, and the corresponding count of movies within each 
combination of film category for each corresponding rental duration 
category. The resulting table should have three columns:
- Category
- Rental length category
- Count
*/

WITH duration_cte AS (
	SELECT rental_id
		, inventory_id
		, DATE_PART('day',return_date - rental_date) AS rental_duration
		-- finding duration of each rental for all categories
	FROM rental
	WHERE rental_date IS NOT NULL
		AND return_date IS NOT NULL
)

, movie_rental_durations AS (
	SELECT b.film_id
		-- , a.rental_id
		, c.title AS film_title
		, AVG(a.rental_duration) AS avg_rental_duration_per_movie
	FROM duration_cte a
	INNER JOIN inventory b
		ON b.inventory_id = a.inventory_id
	INNER JOIN film c
		ON c.film_id = b.film_id
	GROUP BY 1,2
)

, quartiles_cte AS (
	SELECT film_title
		, a.film_id
		, c.name AS category_name
		-- , inventory_id
		, avg_rental_duration_per_movie
		, NTILE(4) OVER (ORDER BY avg_rental_duration_per_movie) AS quartile
		-- grouping each rental into a quartile for rental duration
	FROM movie_rental_durations a
	INNER JOIN film_category b
		ON a.film_id = b.film_id
	INNER JOIN category c
		ON b.category_id = c.category_id
)

, results AS (
	SELECT film_title
		, film_id
		, category_name
		, avg_rental_duration_per_movie
		, quartile
	FROM quartiles_cte
	WHERE category_name IN ('Animation',
		'Children',
		'Classics',
		'Family',
		'Comedy',
		'Music')
)

SELECT category_name
	, quartile
	, COUNT(DISTINCT film_id) AS film_count
FROM results
GROUP BY 1,2
ORDER BY 1,2
;

-- Set #2 Question 1
/*
We want to find out how the two stores compare in their count of rental
orders during every month for all the years we have data for. Write a 
query that returns the store ID for the store, the year and month and 
the number of rental orders each store has fulfilled for that month. 
Your table should include a column for each of the following: year, 
month, store ID and count of rental orders fulfilled during that month.
*/

SELECT a.staff_id
	, b.store_id
    , DATE_PART('year', a.rental_date) AS rental_year
    , DATE_PART('month', a.rental_date) AS rental_month
	, COUNT(a.rental_id)
FROM rental a
INNER JOIN staff b
	ON b.staff_id = a.staff_id
GROUP BY 1,2,3,4
ORDER BY 3,4
;

-- Set #2 Question 2
/*
We would like to know who were our top 10 paying customers, how many 
payments they made on a monthly basis during 2007, and what was the 
amount of the monthly payments. Can you write a query to capture the 
customer name, month and year of payment, and total payment amount for
each month by these top 10 paying customers?
*/


WITH top_10_paying_customers AS (
  	SELECT a.customer_id
		, b.email AS customer_email
		, b.first_name || ' ' || b.last_name AS customer_full_name
	    , COUNT(a.payment_id) AS payment_count
	    , SUM(a.amount) AS total_amount_spent
	FROM payment a
	INNER JOIN customer b
		ON b.customer_id = a.customer_id
	GROUP BY 1, 2, 3
	ORDER BY 4 DESC, 3 DESC
	LIMIT 10
)

SELECT a.customer_full_name
	, DATE_TRUNC('month', b.payment_date) AS payment_month
	, COUNT(b.payment_id) AS monthly_payments
	, SUM(b.amount) AS monthly_spend
FROM payment b
INNER JOIN top_10_paying_customers a
	ON b.customer_id = a.customer_id
GROUP BY 1,2
