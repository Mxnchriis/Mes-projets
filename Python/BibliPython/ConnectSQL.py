import mysql.connector  # Correction de l'importation

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='bibli',
            user='root',
            password='First-In-Slot972'
        )
        return connection  # Retourner la connexion
    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion à MySQL : {err}")
        return None  # Retourner None en cas d'erreur

def fetch_data_from_table():
    connection = connect_to_mysql()  # Utilisation de la fonction de connexion
    if connection is not None:  # Vérification si la connexion a réussi
        try:
            cursor = connection.cursor()
            # Exécution d'une requête SELECT
            cursor.execute("SELECT * FROM users;")
            result = cursor.fetchall()
            return result  # Retourner les résultats
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'exécution de la requête : {err}")
        finally:
            cursor.close()  # Toujours fermer le curseur
            connection.close()  # Toujours fermer la connexion
