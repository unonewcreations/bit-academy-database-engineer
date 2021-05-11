-- wijzigen data
UPDATE tabelnaam
SET kolomnaam = 'waarde'
WHERE kolomnaam = 'initiele waarde';

-- verwijderen kolom
ALTER TABLE tabel
DROP kolom;

-- toevoegen nieuwe maan
INSERT INTO planeten (naam, diameter, afstand, massa)
VALUES  
("Mars", 7777, 2255889977, 0);

-- wijzig naam nieuwe maan
UPDATE planeten
SET naam = 'Teenalp'
WHERE id = '6';

-- Welke series hebben een award hebben gewonnen?
SELECT has_won_awards, title 
FROM series 
WHERE has_won_awards = '1';
-- Welke series hebben een cijfer boven de 2.5?
SELECT rating, title 
FROM series 
WHERE rating > '2.5';
-- Welke series zijn in Nederland gemaakt én zijn Nederlands gesproken?
SELECT country, language, title 
FROM series 
WHERE country = 'NL' AND language = 'NL';
-- Welke series hebben minder dan 5 seizoenen?
SELECT seasons, title 
FROM series 
WHERE seasons <= '5';
-- Wat is het hoogste cijfer dat een serie heeft?
SELECT title, MAX(rating) AS HighestRating
FROM series;
-- Welke series hebben minder dan 3 seizoenen of meer dan 20?
SELECT title, seasons
FROM series
WHERE seasons <= '3' OR seasons >= '20';
-- Welke series hebben de lettercombinatie 'Th' in hun title?
SELECT title
FROM series
WHERE title LIKE '%Th%';
-- Welke series hebben geen 3 seizoenen?
SELECT title, seasons
FROM series
WHERE seasons < '3' OR seasons > '3';

