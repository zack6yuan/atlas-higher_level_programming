-- Lists the number of records with the same score in the table "secod_table"
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;