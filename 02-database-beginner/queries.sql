-- Selecteer alle series uit de series tabel
SELECT * FROM `series`;

-- Er zijn 8 aparte queries, of minimaal 5 indien er gebruikt gemaakt wordt van subqueries.
-- Het resultaat van alle queries is juist.
-- Alle queries zijn 'select' queries.
-- Er wordt **niet** op specifieke ID's geselecteerd.
-- Welke series hebben een award hebben gewonnen?
SELECT title 
FROM series 
WHERE has_won_awards > '0';
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
WHERE seasons < '5';
-- Wat is het hoogste cijfer dat een serie heeft?
SELECT MAX(rating) AS HighestRating
FROM series;
-- Welke series hebben minder dan 3 seizoenen of meer dan 20?
SELECT title, seasons
FROM series
WHERE seasons < '3' OR seasons > '20';
-- Welke series hebben de lettercombinatie 'Th' in hun title?
SELECT title
FROM series
WHERE title LIKE '%Th%';
-- Welke series hebben geen 3 seizoenen?
SELECT title, seasons
FROM series
WHERE seasons < > '3';

-- Alle drie de queries maken gebruik van de `order by` clausule om de data te sorteren.
-- Welke series, gesorteerd van hoogste cijfer naar laagste cijfer, hebben een cijfer boven de 2.5?
SELECT title, rating
FROM series
WHERE rating > '2.5'
ORDER BY rating DESC;
-- Welke series hebben minder dan 5 seizoenen, gesorteerd van minste aantal seizoenen naar meeste aantal seizoenen?
SELECT title, seasons
FROM series
WHERE seasons < '5'
ORDER BY seasons ASC; 
-- Welke series hebben minder dan 3 seizoenen of meer dan 20, gesorteerd op aantal seizoenen en land van herkomst?
SELECT title, seasons, country
FROM series
WHERE seasons < '3' OR seasons > '20'
ORDER BY seasons, country;

