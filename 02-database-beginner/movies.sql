-- Ontwerp een nieuwe table genaamd films waar films in kunnen komen te staan. Per film willen we de volgende data opslaan:
-- een uniek volgnummer (verplicht/not null)
-- titel (verplicht/not null)
-- duur (verplicht/not null)
-- datum van uitkomst (optioneel)
-- land van uitkomst (optioneel)
-- omschrijving (verplicht/not null)
-- id van de trailer op youtube (staat in de url achter de v=) (verplicht/not null)
-- Schrijf een 'create table' script voor de films tabel
-- Met een lege tabel kunnen we weinig. Schrijf een insert query die ten minste 5 en maximaal 10 films toevoegt.
USE netland;

CREATE TABLE films (
    id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titel VARCHAR(100) NOT NULL,
    duur DECIMAL(3,2) NOT NULL,
    datum_van_uitkomst DATE,
    land_van_uitkomst VARCHAR(50),
    omschrijving TEXT NOT NULL,
    id_van_de_trailer VARCHAR(100) NOT NULL
);

INSERT INTO films
(titel, duur, datum_van_uitkomst, land_van_uitkomst, omschrijving, id_van_de_trailer)
VALUES
('The Shawshank Redemption', 2.22, '1994-01-02', 'US', 'Twee gevangen mannen krijgen na een aantal jaren een band met elkaar en vinden troost en uiteindelijk verlossing door daden van normaal fatsoen.', 'AL6r-lOJbic'),
('The Godfather', 2.55, '1972-02-02', 'US', 'De ouder wordende patriarch van een georganiseerde misdaaddynastie draagt de controle over zijn clandestiene imperium over aan zijn onwillige zoon.', 'sY1S34973zA'),
('The Dark Knight', 2.32, '2008-02-02', 'US', 'Wanneer het gevaar bekend als de Joker verwoesting en chaos aanricht onder de mensen van Gotham moet Batman een van de grootste psychologische en fysieke tests ondergaan van zijn vermogen om onrecht te bestrijden.', 'TQfATDZY5Y4'),
('The Intouchables', 1.52, '2012-02-02', 'FR', 'Nadat hij door een paragliding ongeluk quadriplegisch is geworden, huurt een aristocraat een jongeman uit het project om zijn verzorger te worden.', '34WIbmXkewU'),
('Oldeuboi', 2.00, '2003-02-02', 'KOR', 'Na vijftien jaar ontvoerd te zijn en gevangen te hebben gezeten, wordt Oh Dae-Su vrijgelaten, maar hij moet zijn ontvoerder binnen vijf dagen vinden.', '2HkjrJ6IK5E');
