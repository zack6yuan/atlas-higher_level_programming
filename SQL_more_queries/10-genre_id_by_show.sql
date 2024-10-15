-- Lists all shows contained in "hbtn_0_tvshows"
-- Requirement: must have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres
WHERE 