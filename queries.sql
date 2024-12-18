create database sport;

create table coaches
(
    id               serial primary key,
    name             varchar,
    status           varchar,
    experience_years int
);

-- drop table coaches cascade;

create table teams
(
    id       serial primary key,
    name     varchar,
    coach_id int unique references coaches (id)
);

alter table teams
    add column point int default 0;

drop table teams cascade;

create table players
(
    id       serial primary key,
    name     varchar,
    team_id  int references teams (id),
    position varchar
);

drop table players;
create table matches
(
    id         serial primary key,
    team1_id   int references teams (id),
    team2_id   int references teams (id),
    score1     int,
    score2     int,
    match_date date
);
drop table matches cascade;

insert into teams (name, coach_id)
values ('Liverpool', 1),
       ('Real madrid', 2),
       ('Man city', 3),
       ('Chelse', 4),
       ('Arsenal', 5),
       ('Barselona', 6),
       ('Paxtakor', 7),
       ('Nasaf', 8),
       ('Xorazm', 9),
       ('Lans', 10);
