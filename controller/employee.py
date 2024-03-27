from flask import jsonify

from model.employee import EmployeeDAO
class Employee:
    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['eid'] = t[0]
            D['hid'] = t[1]
            D['fname'] = t[2]
            D['lname'] = t[3]
            D['age'] = t[4]
            D['position'] = t[5]
            D['salary'] = t[6]
            result.append(D)

        return result

    def make_json_one(self,employee):
        result = {}
        result['eid'] = employee[0]
        result['hid'] = employee[1]
        result['fname'] = employee[2]
        result['lname'] = employee[3]
        result['age'] = employee[4]
        result['position'] = employee[5]
        result['salary'] = employee[6]

        return result
    def getAllEmployees(self):
        model = EmployeeDAO()
        result = model.getAllEmployees()
        answer = self.make_json(result)
        return answer

    def getEmployeeById(self,eid):
        dao = EmployeeDAO()
        employee = dao.getEmployeeById(eid)
        if not employee:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(employee)
            return result