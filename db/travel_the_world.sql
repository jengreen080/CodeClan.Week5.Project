DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR (255)
);

CREATE TABLE places (
    place_id SERIAL PRIMARY KEY,
    place_name VARCHAR(255),
    country_id INT REFERENCES countries(country_id) ON DELETE CASCADE,
    place_description VARCHAR(255),
    visited BOOLEAN
);