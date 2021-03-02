-- list join --

SELECT tv.name as genre, COUNT(genre_id) as number_of_shows 
FROM tv_genres tv
RIGHT JOIN tv_show_genres genre
ON tv.id = genre.genre_id
GROUP BY tv.name
ORDER BY number_of_shows DESC;

