CREATE TABLE clean_vehicle_sales (
    year INT,
    make VARCHAR(50),
    model VARCHAR(50),
    trim VARCHAR(50),
    body VARCHAR(50),
    transmission VARCHAR(50),
    vin VARCHAR(50),
    state VARCHAR(20),
    condition FLOAT,
    odometer FLOAT,
    color VARCHAR(30),
    interior VARCHAR(30),
    seller VARCHAR(100),
    mmr FLOAT,
    sellingprice FLOAT,
    saledate DATETIMEOFFSET,
    car_age INT
);

-- Total rows
SELECT COUNT(*) FROM clean_vehicle_sales;

-- Average selling price by make
SELECT make, AVG(sellingprice) AS avg_price
FROM clean_vehicle_sales
GROUP BY make
ORDER BY avg_price DESC;

-- Top states by sales volume
SELECT state, COUNT(*) AS total_sales
FROM clean_vehicle_sales
GROUP BY state
ORDER BY total_sales DESC;
