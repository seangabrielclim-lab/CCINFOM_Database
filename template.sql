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
    product_code INT,
    FOREIGN KEY (product_code) REFERENCES drugs_record(product_code),
    quantity INT DEFAULT 0,
    date_received DATE,
    recent_date_received DATE,
    quantity_received INT DEFAULT 0,
    shipping_code INT,
    FOREIGN KEY (shipping_code) REFERENCES transportation_record(shipping_code),
    resupply_status ENUM('complete', 'incomplete', 'locked') DEFAULT 'incomplete',
    resupply_id INT
    
);

create table customers(
	customer_code INT PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    contact_number VARCHAR(20),
    customer_type ENUM ('illegal', 'legal') DEFAULT 'legal',
    registration_date DATE
);

create table sales_record(
	transaction_code INT PRIMARY KEY,
    product_code INT,
    FOREIGN KEY (product_code) REFERENCES drugs_record(product_code),
    shipping_code INT,
    FOREIGN KEY (shipping_code) REFERENCES transportation_record(shipping_code),
    customer_code INT,
    FOREIGN KEY (customer_code) REFERENCES customers(customer_code),
    quantity_sold INT DEFAULT 0,
    date_sold DATE
);

CREATE TABLE transportation_record (
    shipping_code INT PRIMARY KEY,
    delivery_company_name VARCHAR(150) NOT NULL,
    transportation_method ENUM('air', 'sea', 'land') NOT NULL,
    transported_quantity INT NOT NULL,

    origin_country VARCHAR(100) NOT NULL,
    origin_city VARCHAR(100) NOT NULL,

    destination_country VARCHAR(100) NOT NULL,
    destination_city VARCHAR(100) NOT NULL,

    dispatch_date DATE NOT NULL,
    expected_delivery_date DATE NOT NULL,
    actual_delivery_date DATE,

    delivery_status ENUM(
        'preparing',
        'packaged',
        'en route',
        'partial',
        'completed'
	) NOT NULL DEFAULT 'preparing',
    shipping_cost DECIMAL(10,2) NOT NULL,
    delivery_type ENUM('resupply', 'order') NOT NULL,
    transaction_code INT,
	FOREIGN KEY (transaction_code) REFERENCES sales_record(transaction_code)
);