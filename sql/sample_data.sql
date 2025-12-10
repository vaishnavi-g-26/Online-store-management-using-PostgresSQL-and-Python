-- ==============================================
-- SAMPLE DATA FOR ONLINE STORE MANAGEMENT SYSTEM
-- ==============================================

-- INSERT SAMPLE PRODUCTS
INSERT INTO products (p_name, price, stock) VALUES
('Sandals', 800.00, 20),
('Women Clothes', 1800.00, 15),
('Watches', 2500.00, 10),
('Purses', 1200.00, 12),
('Rings', 900.00, 8);

-- INSERT SAMPLE CUSTOMERS
INSERT INTO customers (customer_name, phone) VALUES
('Alice', '9999000000'),
('Bob', '8888000000'),
('Rahul', '9988776655');

-- INSERT SAMPLE ORDERS
INSERT INTO orders (customer_id, total_amount, status) VALUES
(1, 1600.00, 'Shipped'),
(2, 2500.00, 'Pending');

-- INSERT SAMPLE ORDER ITEMS
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 2, 800.00),   -- Alice bought 2 Sandals
(2, 3, 1, 2500.00);  -- Bob bought 1 Watch
