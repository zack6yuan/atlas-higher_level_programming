-- Creates database "hbtn_0d_2" and the user "user_0d_2"
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISETS 'user_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 * TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;