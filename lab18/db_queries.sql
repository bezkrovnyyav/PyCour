/* 1.1 Noncorrelated and Correlated Subqueries in Select */

SELECT id, content, (SELECT ROUND(AVG(LENGTH(content)), 1) FROM posts) AS len_content FROM posts;

SELECT p.id, p.title, p.content, (SELECT COUNT(*) FROM photos WHERE p.id = photos.post_id) AS num_photos FROM posts AS p;

/* 1.2 Write at least one From clause with subquery in it */

SELECT id, username, title FROM (SELECT  u.id, u.username, p.title FROM users AS u, posts AS p WHERE u.id = p.user_id) AS users_posts;

/* 1.3 Write at least one Where clause with subquery in it */

SELECT u.id, u.username FROM users AS u WHERE(SELECT count(*) FROM comments AS uc WHERE u.id = uc.user_id) >= 1;

/* 1.4 Use WITH clause (Common Table Expression) */

WITH user AS (SELECT id, username FROM users WHERE id = 2) SELECT username FROM user; 

/* 1.5 Group the data by some field and filter it with Having clause */

SELECT u.id, u.username, count(*) AS count_comments FROM users AS u INNER JOIN comments AS c ON u.id = c.user_id GROUP BY u.id HAVING COUNT(*) > 1;

/* 1.6 Use Order by */

SELECT * FROM comments ORDER BY user_id;

/* 1.7 Use Limit */

SELECT * FROM comments ORDER BY user_id LIMIT 3;

/* 2. Add queries that work with multiple table to retrieve the data from you database*/

/* 2.1 INNER, LEFT, RIGHT, OUTER joins */

SELECT u.username, p.content FROM users AS u INNER JOIN posts AS p ON u.id = p.user_id GROUP BY u.id ORDER BY u.id;

SELECT u.username, p.content FROM users AS u LEFT JOIN posts AS p ON u.id = p.user_id LIMIT 3;

/* SQLite hasn't implemented RIGHT OUTER or FULL OUTER */

/* 2.2 USING */

SELECT c.title, ph.path_to_photo FROM categories AS c JOIN photos AS ph USING (post_id);

/* 2.3 NATURAL JOIN */

SELECT u.username, p.content FROM users AS u NATURAL JOIN posts AS p;


/* 2.4 CROSS JOIN*/

SELECT u.username, c.content FROM users AS u CROSS JOIN comments as c LIMIT 3;

/* 2.5 SELF JOIN */

SELECT p1.id, p1.content, p2.id, p2.content FROM posts AS p1, posts AS p2 WHERE p1.user_id <> p2.user_id LIMIT 5;

/* 2.6 UNION */

SELECT id, username FROM users UNION SELECT id, content FROM comments;

/* 2.7 EXCEPT and INTERSECT */

SELECT u.id, u.username FROM users AS u WHERE id = (SELECT u.id EXCEPT SELECT p.user_id FROM posts AS p);

SELECT c.user_id FROM comments AS c INTERSECT SELECT p.user_id FROM posts AS p;

/* 2.8 ROLLBACK */

INSERT INTO photos (post_id, path_to_photo) VALUES (5, "wrong path");  
SELECT * FROM photos;
ROLLBACK;
SELECT * FROM photos;

/* 3 Add statements to work with the db.*/
/* 3.1 transactions (at least 2) */

BEGIN TRANSACTION; 
INSERT INTO comments (user_id, content) VALUES (1, "Comments about Java"); 
COMMIT;

BEGIN TRANSACTION;
UPDATE comments SET content = "Comments about Java and Python" WHERE user_id = 1;
COMMIT;

/* 3.2 coalesce */

SELECT u.id, u.username, coalesce(p.content, 'no posts') FROM users AS u LEFT JOIN posts AS p ON u.id = p.user_id LIMIT 3;

/* 3.3 cast */

SELECT id, content, CAST(created_time AS DATE) FROM comments LIMIT 15;

/* 3.4 case when */

SELECT u.id, u.username, p.title FROM users AS u LEFT JOIN posts AS p ON u.id = p.user_id;

/* 3.5 use different datetime functions */
SELECT id, title, created_time,  DATE(created_time), TIME(created_time), CURRENT_TIME FROM posts;
