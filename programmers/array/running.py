def solution_long_time(players, callings):
    answer = players
    
    for call in callings:
        idx = answer.index(call)

        # Swap
        tmp = answer[idx]
        answer[idx] = answer[idx-1]
        answer[idx-1] = tmp
    
    return answer


def solution(players, callings):    
    rank_player, player_rank = dict(), dict()
    for i, k in enumerate(players):
        player_rank[k] = i
        rank_player[i] = k
    
    for c in callings:
        runner = c
        runner_idx = player_rank[c]
        preceder = rank_player[runner_idx-1]
        preceder_idx = runner_idx-1

        player_rank[runner] = preceder_idx
        player_rank[preceder] = runner_idx
        rank_player[runner_idx] = preceder
        rank_player[preceder_idx] = runner
    
    answer = [runner for _, runner in rank_player.items()]

    return answer


def main():
    test()


def test():
    players = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]
    target = ["mumu", "kai", "mine", "soe", "poe"]
    result = solution(players, callings)
    print("target: {}\nresult: {}\n{}".format(target, result, 'Pass' if target==result else 'Fail'))


if __name__ == '__main__':
    main()