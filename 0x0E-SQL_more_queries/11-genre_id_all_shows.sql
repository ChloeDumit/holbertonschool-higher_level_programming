-- list join --

SELECT t.title, tg.genre_id
FROM tv_shows_genres tg
RIGHT OUTER JOIN tv_shows t
ON t.id = tg.show_id
ORDER BY t.title, tg.genre_id ASC;