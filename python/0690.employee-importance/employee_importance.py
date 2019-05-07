#https://leetcode.com/problems/employee-importance/

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

def getImportance(employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    emps = {employee.id: employee for employee in employees}
    dfs = lambda id: sum([dfs(sub_id) for sub_id in emps[id].subordinates]) + emps[id].importance
    return dfs(id)
    

def getImportance(employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    graph = { emp.id: (emp.importance, emp.subordinates) for emp in employees }
    answer, Q = 0, [id]
    while Q:
        answer += sum(graph[i][0] for i in Q)
        Q = [sub for e_id in Q for sub in graph[e_id][1]]
    return answer
