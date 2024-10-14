-- Creates the database "hbtn_0d_usa" and the table "cities" in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE AUTO INCREMENT NOT NULL PRIMARY KEY;
    state_id INT NOT NULL FOREIGN KEY(state_id) REFERENCES (state_id);
    name VARCHAR(256) NOT NULL;
)