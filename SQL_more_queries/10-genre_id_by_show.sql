-- Lists all shows contained in "hbtn_0_tvshows"
-- Requirement: must have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_shows.genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id