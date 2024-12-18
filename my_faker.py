from dataclasses import dataclass
import faker
from main import PG

f = faker.Faker()


@dataclass
class Coache(PG):
    id: int = None
    name: str = None
    status: str = None
    experience_years: int = None


def join_coach(count: int = 0) -> None:
    dp = ['win', 'draw', 'lost']
    while count != 10:
        coach = {
            'name': f.first_name(),
            'status': f.random_choices(dp, 1)[0],
            'experience_years': f.random_int(1, 10)
        }
        count += 1
        Coache(**coach).save()


# join_coach()


@dataclass
class Player(PG):
    id: int = None
    name: str = None
    team_id: int = None
    position: str = None

def join_player(count = 0):
    dp = ['attacker', 'midfielder', 'protector', 'gatekeeper']
    counter = 0
    while count != counter:
        player = {
            'name' : f.first_name(),
            'team_id' : f.random_int(1, 10),
            'position' : f.random_choices(dp, 1)[0]
        }
        counter += 1
        Player(**player).save()
# join_player(100)


@dataclass
class Matche(PG):
    id: int = None
    team1_id: int = None
    team2_id: int = None
    score1: int = None
    score2: int = None
    match_date: str = f.date()


def join_match(count = 0):
    counter = 0
    while count != counter:
        match = {
            'team1_id': f.random_int(1, 10),
            'team2_id': f.random_int(1, 10),
            'score1': f.random_int(0, 3),
            'score2': f.random_int(0,3),
            'match_date': f.date(),
        }
        if match['team1_id'] != match['team2_id']:
            if match['score1'] == 1 and match['score2'] == 1:
                Matche(**match).save()
                counter += 1
            if (match['score1'] == 0 and match['score2'] == 3) or (match['score1'] == 3 and match['score2'] == 0):
                Matche(**match).save()
                counter += 1

# join_match(50)

