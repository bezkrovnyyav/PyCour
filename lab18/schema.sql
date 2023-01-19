CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(30) NOT NULL UNIQUE,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    status VARCHAR(30) DEFAULT "user" CHECK (status IN ("user", "writer", "admin")),
	password_user VARCHAR(80),
    email VARCHAR(30) NOT NULL UNIQUE CHECK (
		email LIKE '%_@__%.__%' AND
		LENGTH(email) - LENGTH(REPLACE(email, '@', '')) = 1 AND
		SUBSTR(LOWER(email), INSTR(email, '.') + 1) NOT GLOB '*[^a-z]*'
	)  
);

INSERT INTO users
       (username, first_name, last_name, status,  email, password_user)
VALUES ("Neo", "Richard", "Hendricks", "admin", "hendricks@ukr.net", "pass1"),
       ("Trinity", "Monica", "Hall", "writer", "m_hall@ukr.net", "pass1"),
       ("Morpheus", "Bertram", "Gilfoyle", "writer", "gilfoyle@ukr.net", "pass3") ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS comments (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users (id),
    content VARCHAR(150) NOT NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO comments
       (user_id, content)
VALUES (3, "Comments about Data Base"),
       (2, "Comments about Python"),
       (1, "Comments about JavaScript") ON CONFLICT DO NOTHING;
	   
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users (id),
    title VARCHAR(30) NOT NULL,
    content VARCHAR(150) NOT NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO posts
       (user_id, title, content)
VALUES (3, "Data Base", "About Data Base"),
       (2, "Python", "About Python"),
       (1, "JavaScript", "About JavaScript") ON CONFLICT DO NOTHING;
	   
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    title VARCHAR(30) NOT NULL,
    description VARCHAR(150) NOT NULL,
	CONSTRAINT categories_posts_fk 
	FOREIGN KEY (post_id) REFERENCES posts (id)
);

INSERT INTO categories
       (post_id, title, description)
VALUES (1, "Data Base", "About Data Base"),
       (2, "Python", "About Python"),
       (3, "JavaScript", "About JavaScript") ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS photos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER REFERENCES posts (id),
    path_to_photo VARCHAR(80) NOT NULL
);

INSERT INTO photos
       (post_id, path_to_photo)
VALUES (1, "./photos/DB.png"),
       (2, "./photos/Python.png"),
       (3, "./photos/JS.png") ON CONFLICT DO NOTHING;

CREATE INDEX IF NOT EXISTS index_user_email ON users (username, email);

DROP VIEW IF EXISTS users_info;

CREATE VIEW IF NOT EXISTS users_info AS SELECT
    users.username,
	users.first_name,
    users.last_name,
    users.email,
	users.status,
    COUNT(DISTINCT posts.id) count_posts,
    COUNT(DISTINCT comments.id) count_comments
    FROM users LEFT JOIN posts
    ON posts.user_id = users.id
    LEFT JOIN comments
    ON comments.user_id = users.id
	GROUP BY users.id;
	