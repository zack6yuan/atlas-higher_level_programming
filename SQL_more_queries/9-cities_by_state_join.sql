-- Lists all cities contained in the databse "hbtn_0d_usa"
SELECT cities.id, cities.name, states.name FROM cities
JOIN cities.state_id = states.id
ORDER BY cities.id;