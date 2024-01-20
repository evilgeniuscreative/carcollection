CREATE DATABASE vehiclesdb;
CREATE USER collector WITH PASSWORD 'vroom';
GRANT ALL PRIVILEGES ON DATABASE vehiclesdb TO collector;
ALTER DATABASE vehiclesdb OWNER TO collector;