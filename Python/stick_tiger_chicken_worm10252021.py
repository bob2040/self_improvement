import random


def stick_tiger_chicken_worm():
    p_win_c = 0
    r_win_c = 0
    draw = 0
    invalid = 0
    n = 0
    while True:
        r = random.randint(0, 3)
        if r == 0:
            robot = 'stick'
        elif r == 1:
            robot = 'tiger'
        elif r == 2:
            robot = 'chicken'
        else:
            robot = 'worm'
        player = input(f'Round {n+1},please show your card:')
        if player != 'stick' and player != 'tiger' and player != 'chicken' and player != 'worm':
            print('You made a typing error just now!')
            continue
        p1 = (player == 'stick')
        p2 = (player == 'tiger')
        p3 = (player == 'chicken')
        p4 = (player == 'worm')
        r1 = (robot == 'stick')
        r2 = (robot == 'tiger')
        r3 = (robot == 'chicken')
        r4 = (robot == 'worm')
        rounds_were_draws = 'rounds were draws' if draw >= 2 else 'round was a draw'
        rounds_were_invalid = 'rounds were invalid' if invalid >= 2 else 'round was invalid'
        if (p1 and r2) or (p2 and r3) or (p3 and r4) or (p4 and r1):
            n += 1
            p_win_c += 1
            rounds_p = 'rounds' if p_win_c >= 2 else 'round'
            print(f'Bob:[{player}],Python:[{robot}].Bob wins this round!Bob has won {p_win_c} {rounds_p}.')
            if p_win_c >= 2 and p_win_c > r_win_c:
                print(f'{n} rounds in total:Bob won {p_win_c} rounds,Python won {r_win_c} round,{draw} {rounds_were_draws},{invalid} {rounds_were_invalid}.Final:Bob Wins!')
                print('Game is over!')
                break
        elif (p1 and r1) or (p2 and r2) or (p3 and r3) or (p4 and r4):
            n += 1
            draw += 1
            print(f'Bob:[{player}],Python:[{robot}].This round is a draw!')
        elif (r1 and p2) or (r2 and p3) or (r3 and p4) or (r4 and p1):
            n += 1
            r_win_c += 1
            rounds_r = 'rounds' if r_win_c >= 2 else 'round'
            print(f'Bob:[{player}],Python:[{robot}].Python wins this round!Python has won {r_win_c} {rounds_r}.')
            if r_win_c >= 2 and r_win_c > p_win_c:
                print(f'{n} rounds in total:Bob won {p_win_c} round,Python won {r_win_c} rounds,{draw} {rounds_were_draws},{invalid} {rounds_were_invalid}.Final:Python Wins!')
                print('Game is over!')
                break
        else:
            n += 1
            invalid += 1
            print(f'Bob:[{player}],Python:[{robot}].This round is invalid!')


stick_tiger_chicken_worm()
