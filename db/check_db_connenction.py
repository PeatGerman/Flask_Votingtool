from sqlalchemy import text


def test_db_connection(engine):
    try:

        # Verbindung herstellen und kleine Abfrage durchführen
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("connection succes")
        # Wenn dies ohne Fehler durchläuft, konnte die Verbindung hergestellt werden
        return True
    except Exception as e:
        print(f'Error occurred while connecting to the database: {e}')
        return False


