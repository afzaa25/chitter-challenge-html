from lib.peep import Peep

class PeepRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from peeps')
        peeps = []
        for row in rows:
            # print(type(row['date_created']))
            peep = Peep(row['id'], row['message'], str(row['date_created']), row['user_id']) 
            peeps.append(peep)
        return peeps
    

    def find(self, peep_id):
        rows = self._connection.execute('SELECT * FROM peeps WHERE id = %s', [peep_id])
        row = rows[0]
        return Peep(row['id'], row['message'], str(row['date_created']), row['user_id'])

    def create(self, peep):
        self._connection.execute('INSERT INTO peeps(message, date_created, user_id) VALUES (%s, %s, %s)', [peep.message, peep.date_created, peep.user_id])
        return None
    

    def delete(self, peep_id):
        self._connection.execute('DELETE FROM peeps WHERE id = %s', [peep_id])
        return None
