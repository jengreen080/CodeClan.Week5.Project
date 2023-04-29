DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS countries;

CREATE TABLE places (
    place_id SERIAL PRIMARY KEY,
    place_name VARCHAR(255),
    country VARCHAR(255),
    place_description VARCHAR(255),
    status VARCHAR(255)
);
-- does country need defined as foreign key?

CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR (255)
);