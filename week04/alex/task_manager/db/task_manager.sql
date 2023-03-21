-- DROP TABLE IF EXISTS tasks;

-- CREATE TABLE tasks (
--   id SERIAL PRIMARY KEY,
--   description VARCHAR(255),
--   assignee VARCHAR(255),
--   duration INT,
--   completed BOOLEAN DEFAULT FALSE
-- );

-- INSERT INTO tasks (description, assignee, duration) 
-- VALUES ('Walk Dog', 'Jack Jarvia', 60);

-- INSERT INTO tasks (description, assignee, duration) 
-- VALUES ('Feed Cat', 'Victor McDade', 5);

DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  duration INT,
  completed BOOLEAN,
  user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE
);
-- Without ON DELETE CASCADE, when we delete the user, the whole tasks table will be deleted