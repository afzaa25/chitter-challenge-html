DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text
);

INSERT INTO users (username, email, password) VALUES ('afzaa25', 'afzaaatcha25@gmail.com', 'Password123!');
INSERT INTO users (username, email, password) VALUES ('atcha25', 'atcha25@gmail.com', 'Password1234!');


CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    message text,
    date_created date,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO peeps (message, date_created, user_id) VALUES ('Hi, this is my first peep', '2023-05-25', 1);
INSERT INTO peeps (message, date_created, user_id) VALUES ('Hi, this is my second peep', '2023-05-26', 1);

