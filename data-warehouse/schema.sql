CREATE TABLE orders_streaming (
    event_time VARCHAR(50),
    order_id VARCHAR(20),
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    qty INT,
    unit_price FLOAT,
    total_amount FLOAT
);

