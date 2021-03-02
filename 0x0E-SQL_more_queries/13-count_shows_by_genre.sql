-- list join --

SELECT name as genre, COUNT(genre_id) as number_of_shows 
FROM tv_genres
RIGHT JOIN tv_show_genres
ON id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;

