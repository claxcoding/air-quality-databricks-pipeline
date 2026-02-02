Data Model

Bronze Table (Raw Live Data)
field	type	description
sensor_id	string	Unique sensor identifier
timestamp	string	ISO timestamp from sensor
sensor_type	string	e.g., SDS011, BME280
value_type	string	e.g., PM10, temperature
value	double	Measured value
location	struct	lat / lon

Bronze Table (Historic CSV)
field	type
sensor_id	string
timestamp	timestamp
lat	double
lon	double
P1	double
P2	double
temperature	double
humidity	double
pressure	double
Silver Table

Enforced schema

Converted timestamps

Flattened sensor types

Deduplicated entries

Gold Table

Examples:

Daily PM10 averages per city

Sensor uptime%

Temperature trends

High-pollution alerts