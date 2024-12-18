-- task 3

-- select  t.name, count(m.score1) p from teams t
-- inner join matches m on t.id = m.team1_id group by t.name order by p desc ;

select t.name, count(m2.score2 + m.score1) point
from teams t
         inner join matches m on t.id = m.team1_id
         inner join matches m2 on t.id = m2.team2_id
group by t.name
order by point desc;


-- task 4

CREATE or replace FUNCTION add_point_func()
    RETURNS TRIGGER
    LANGUAGE PLPGSQL
AS
$$
BEGIN
    insert into matches (team1_id, team2_id, score1, score2, match_date)
    values (new.team1_id, new.team2_id, new.score1, new.score2, new.match_date);
    return new;
END;
$$;


CREATE TRIGGER add_point_triiger
    AFTER insert
    ON matches
    for EACH ROW
EXECUTE FUNCTION add_point_func();



-- task 5

create or replace function coach_win_static()
   returns varchar
   language plpgsql
  as
$$

begin
   select c.status from coaches c where status = 'win';
end;
$$;
drop function coach_win_static();
select coach_win_static();


-- task 6

select t.name Team, p.name, p.position from teams t
inner join players p on t.id = p.team_id order by Team;