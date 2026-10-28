-- Student Course Revenue Analysis (synthetic practice dataset)
-- Import data/student_orders.csv as table student_orders before running.

-- 1. Overall order-status mix
SELECT status, COUNT(*) AS order_count
FROM student_orders
GROUP BY status
ORDER BY order_count DESC;

-- 2. Successful paid revenue by exam category
SELECT exam_category,
       COUNT(*) AS successful_orders,
       SUM(amount_inr) AS successful_revenue_inr
FROM student_orders
WHERE status = 'SUCCESS'
GROUP BY exam_category
ORDER BY successful_revenue_inr DESC;

-- 3. Successful paid revenue by acquisition channel
SELECT acquisition_channel,
       COUNT(*) AS successful_orders,
       SUM(amount_inr) AS successful_revenue_inr
FROM student_orders
WHERE status = 'SUCCESS'
GROUP BY acquisition_channel
ORDER BY successful_revenue_inr DESC;

-- 4. Rank customers by successful paid spend
WITH customer_revenue AS (
    SELECT user_id, SUM(amount_inr) AS revenue_inr
    FROM student_orders
    WHERE status = 'SUCCESS'
    GROUP BY user_id
)
SELECT user_id, revenue_inr,
       RANK() OVER (ORDER BY revenue_inr DESC) AS revenue_rank
FROM customer_revenue
ORDER BY revenue_rank, user_id;

-- 5. Data-quality check: duplicate order IDs
SELECT order_id, COUNT(*) AS row_count
FROM student_orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 6. Check for missing key fields
SELECT
    SUM(CASE WHEN user_id IS NULL OR TRIM(user_id) = '' THEN 1 ELSE 0 END) AS missing_user_id,
    SUM(CASE WHEN status IS NULL OR TRIM(status) = '' THEN 1 ELSE 0 END) AS missing_status
FROM student_orders;
