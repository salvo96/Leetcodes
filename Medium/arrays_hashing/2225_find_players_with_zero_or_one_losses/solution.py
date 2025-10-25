class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_dict = {}
        lose_dict = {}

        for match in matches:
            player1 = match[0]
            player2 = match[1]

            if win_dict.get(player1):
                win_dict[player1] += 1
            else:
                win_dict[player1] = 1

            if lose_dict.get(player2):
                lose_dict[player2] += 1
            else:
                lose_dict[player2] = 1

        for player in lose_dict.keys():
            if lose_dict[player] != 1:
                lose_dict[player] = 0

            if win_dict.get(player):
                win_dict[player] = 0

        return [
            sorted(
                [
                    player_winner
                    for player_winner in win_dict.keys()
                    if win_dict[player_winner] > 0
                ]
            ),
            sorted(
                [
                    player_loser
                    for player_loser in lose_dict.keys()
                    if lose_dict[player_loser] > 0
                ]
            ),
        ]
