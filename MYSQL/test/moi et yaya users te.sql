SELECT * FROM users_schema.users;

-- INSERT INTO users (first_name, last_name) VALUES ("Yaya", "DEMBELE");

UPDATE users
SET first_name = "Raed", last_name = "Doe"
WHERE user_id = 1;