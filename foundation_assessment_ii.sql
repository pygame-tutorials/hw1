CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

-- Create movie_info table
CREATE TABLE movie_info (
  movie_ID INT,
  movie_name VARCHAR(255),
  movie_length TIME,
  age_rating VARCHAR(10)
);

-- Create screens table
CREATE TABLE screens (
  screen_ID INT,
  four_k BOOLEAN
);

-- Create showings table
CREATE TABLE showings (
  showing_ID INT,
  movie_ID INT,
  screen_ID INT,
  start_time TIME,
  available_seats INT
);


USE foundation_assessment_ii;

 INSERT INTO movie_info(movie_ID, movie_name, movie_length, age_rating)
 VALUES 
 (1, "The Movie", "2:19:00", "12A"),
 (2, "The Other Movie", "1:30:00", "15"),
 (3, "The 3D Amazing Movie",  "1:42:00", "PG"),
 (4, "La Allure", "1:09:00", "18"),
 (5, "The Cartoon", "1:15:00", "U"),
 (6, "The Scary Cartoon", "1:23:00", "PG"),
 (7, "The Coming Of Age", "1:40:00", "12A"),
 (8, "The War", "2:07:00", "15"),
 (9, "The Murder Mystery", "1:47:00", "15");

 INSERT INTO screens(screen_ID, four_k)
 VALUES 
  (1, True),
  (2, False),
  (3, True),
  (4, True),
  (5, True),
  (6, True),
  (7, True),
  (8, False),
  (9, True),
  (10, True);

 INSERT INTO showings(showing_ID, movie_ID,screen_ID, start_time, available_seats)
 VALUES 
  (1, 1, 2, '12:00:00', 10), 
  (2, 1, 2, '17:00:00', 23), 
  (3, 2, 9, '10:30:00', 30), 
  (4, 3, 1, '07:00:00', 38), 
  (5, 3, 5, '10:00:00', 26), 
  (6, 3, 1, '17:00:00', 5), 
  (7, 3, 1, '19:00:00', 0), 
  (8, 3, 5, '14:00:00', 2), 
  (9, 4, 9, '20:00:00', 14), 
  (10, 4, 9, '23:00:00', 23), 
  (11, 5, 6, '09:30:00', 30), 
  (12, 5, 6, '12:30:00', 7), 
  (13, 5, 6, '14:30:00', 0), 
  (14, 5, 6, '15:20:00', 0), 
  (15, 6, 10, '10:00:00', 32), 
  (16, 6, 10, '13:30:00', 25), 
  (17, 6, 10, '17:00:00', 14), 
  (18, 7, 7, '12:00:00', 36), 
  (19, 8, 4, '15:00:00', 24), 
  (20, 9, 3, '17:00:00', 0);
-- create inner join between movie info and showings dependent on movie ID
-- with the condition of anything after 12:00:00 and at least 1 seat is greater than 0
-- order in ascending order based on start time
SELECT movie_name, start_time
FROM movie_info
JOIN showings ON movie_info.movie_ID = showings.movie_ID
WHERE start_time > '12:00:00' AND available_seats > 0
ORDER BY start_time;

-- create inner join between movie info and showings table dependent on movie ID
-- group the number of showings for each
-- sorts the movies in descending order dependent on the count of showing
-- only show the movie with the most showings
SELECT movie_name
FROM movie_info
JOIN showings ON movie_info.movie_ID  = showings.movie_ID 
GROUP BY movie_info.movie_ID, movie_info.movie_name
ORDER BY COUNT(*) DESC
LIMIT 1;

