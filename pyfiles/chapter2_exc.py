##### Excercises
#### Chapter 2
### 2.3
def for_the_td(player1, player2):
    return f'{player1} to {player2} for the TD!'


print(for_the_td("Dak", "Zeke"))


### 2.5
def is_leveon(player):
    if player.lower() == "le'veon bell":
        return True
    else:
        return False


### 2.6
def commentary(score):
    if score >= 100:
        return f'{score} is a good score'
    else:
        return f'{score} is not a good score'


### 2.7
list = ["Tom Brady", "LeVeon Bell", "OBJ", "Tyreek Hill"]


def seperate_List(list):
    return ["OBJ" in player for player in list]


print(seperate_List(list))

### 2.8
## A
league_settings = {'number of teams': 12, 'ppr': True}
print(league_settings)
league_settings['number of teams'] = 10;
print(league_settings)


## B
# Python ternary operator: [on_true] if [expression] else [on_false]
def toggle_ppr(input_dict):
    if input_dict['ppr']:
        input_dict['ppr'] = False
    else:
        input_dict['ppr'] = True
    return input_dict


### 2.10
## A
roster_list = ['tom brady', 'adrian peterson', 'antonio brown']
only_last_names = []

for player in roster_list:
    split_name = player.split()
    only_last_names.append(split_name[-1])  # -1 accesses last element

print(only_last_names)

## B
# Dict comprehension from list. {>input for KEY<:>input for VALUE< FOR >element< IN >LIST<}
new_dict = {player: len(player) for player in roster_list}
print(new_dict)

### 2.11
roster_dictionary = {'qb': 'tom brady', 'rb1': 'adrian peterson', 'wr1': 'davante adams', 'wr2': 'john brown'}

## A
only_positions = roster_dictionary.keys()

## B
only_last_names_with_a_b = [player for position, player in roster_dictionary.items() if
                            player.split()[-1][0] in ['a', 'b']]


### 2.12
## A
def mapperWithListComprehension(passedList, passedFunction):
    return [passedFunction(element) for element in passedList]


## B
# Lambda functions -> lambda passeParameter: passedParameter * whatever
rushing_yards = [1, 110, 60, 4, 0, 0, 0]
print(mapperWithListComprehension(rushing_yards, lambda element: element*0.1))