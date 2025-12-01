class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand = sorted(hand)

        hand_dict = {}
        for value in hand:
            if value in hand_dict.keys():
                hand_dict[value] += 1
            else:
                hand_dict[value] = 1

        for card in sorted(hand_dict.keys()):
            if hand_dict[card] > 0:
                need = hand_dict[card]
                for i in range(card, card + groupSize):
                    if hand_dict.get(i, 0) < need:
                        return False
                    hand_dict[i] -= need
        return True
