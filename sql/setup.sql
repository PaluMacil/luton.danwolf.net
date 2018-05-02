CREATE TABLE IF NOT EXISTS observations (
    id serial PRIMARY KEY,
    mac TEXT NULL,
    ipv4 text NOT NULL,
    observation_type text check (observation_type in ('report', 'manual')),
    observation_date date
);