#https://leetcode.com/problems/distribute-candies-to-people/

def distributeCandies(candies, num_people):
    people = num_people * [0]
    give = 0
    while candies > 0:
        people[give % num_people] += min(candies, give + 1)
        give += 1
        candies -= give
    return people
