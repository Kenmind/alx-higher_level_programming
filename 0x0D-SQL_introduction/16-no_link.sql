-- Lists all records of the table "second_table"
	-- without listing rows without a name value
		--in descending order
SELECT score, name FROM second_table
WHERE name != ""
ORDER BY score DESC;
