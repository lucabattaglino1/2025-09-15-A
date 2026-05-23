from database.DB_connect import DBConnect
from model.Driver import Driver


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results


    @staticmethod
    def getAllNodes(anno1, anno2):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT d.driverId, d.forename, d.surname
                    FROM drivers d, results r, races ra
                    WHERE d.driverId = r.driverId 
                    and r.raceId = ra.raceId 
                    and ra.year BETWEEN %s and %s
                    and r.position is not null
                    group by d.driverId, d.forename, d.surname"""

        cursor.execute(query, (anno1, anno2))

        for row in cursor:
            results.append(Driver(row["driverId"], row["forename"], row["surname"]))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(anno1, anno2, idMap):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT d1.driverId as id1, d2.driverId as id2, count(r1.constructorId = r2.constructorId) as peso
                    FROM drivers d1, results r1, races ra1,
                    drivers d2, results r2, races ra2
                    WHERE d1.driverId = r1.driverId 
                    and r1.raceId = ra1.raceId 
                    and ra1.year BETWEEN %s and %s
                    and r1.position is not null
                    and d2.driverId = r2.driverId 
                    and r2.raceId = ra2.raceId 
                    and ra2.year BETWEEN %s and %s
                    and r2.position is not null 
                    and r1.constructorId = r2.constructorId
                    and d1.driverId < d2.driverId 
                    and ra1.raceId = ra2.raceId 
                    group by d1.driverId, d2.driverId"""

        cursor.execute(query, (anno1, anno2, anno1, anno2))

        for row in cursor:
            c1 = idMap[row["id1"]]
            c2 = idMap[row["id2"]]
            peso = row["peso"]
            results.append((c1, c2, peso))

        cursor.close()
        conn.close()
        return results

