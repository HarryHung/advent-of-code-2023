from collections import Counter

strength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

with open("puzzle_input.txt", "r") as input_file:
    hands = [line.split() for line in input_file]

    type_hand_record = {
        'high_card': [],
        'one_pair': [],
        'two_pair': [],
        'three_of_a_kind': [],
        'full_house': [],
        'four_of_a_kind': [],
        'five_of_a_kind': []
    }

    for hand in hands:
        type = sorted(Counter(hand[0]).values())

        match type:
            case [5]:
                type_hand_record['five_of_a_kind'].append(hand)
            case [1, 4]:
                type_hand_record['four_of_a_kind'].append(hand)
            case [2, 3]:
                type_hand_record['full_house'].append(hand)
            case [1, 1, 3]:
                type_hand_record['three_of_a_kind'].append(hand)
            case [1, 2, 2]:
                type_hand_record['two_pair'].append(hand)
            case [1, 1, 1, 2]:
                type_hand_record['one_pair'].append(hand)
            case [1, 1, 1, 1, 1]:
                type_hand_record['high_card'].append(hand)
            case _:
                raise Exception('Unknown card type')
    
    res = 0
    rank = 1

    for hands in type_hand_record.values():
        if not hands:
            continue
        
        for hand, bid in sorted(hands, key=lambda x: [strength.index(c) for c in x[0]]):
            res += int(bid) * rank
            rank += 1
    
    print(res)
    
