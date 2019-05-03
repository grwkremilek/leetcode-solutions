# Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


#### Runtime: 104 ms, faster than 93.65%

Intuition:

Consider trust as a graph, all pairs are directed edge.

The point with in-degree - out-degree = N - 1 become the judge.

Explanation:

Count the degree, and check at the end.

Time Complexity:

Time O(T + N), space O(N)

