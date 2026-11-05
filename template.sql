create table drugs_record(
	product_code INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_price DECIMAL(6, 5) DEFAULT 0.00,
    quantity_in_stock INT DEFAULT 0,
    minimum_stock_level INT DEFAULT 5,
    availability_status BOOLEAN
    
);    

create table resupply_record(
	supply_code INT PRIMARY KEY,
    product_code INT REFERENCES drugs_record(product_code),
    quantity INT DEFAULT 0,
    date_received DATE,
    recent_date_received DATE,
    quantity_received INT DEFAULT 0,
    shipping_code INT REFERENCES transportation_record(shipping_code),
    resupply_status ENUM('complete', 'incomplete', 'locked') DEFAULT 'incomplete',
    resupply_id INT
    
);
SELECT * from drugs_record;    