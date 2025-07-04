def query():
    query = """
    CREATE TABLE IF NOT EXISTS transactions AS SElECT * FROM ledger;
    """
    return query


def query1():
    query1 = """
        CREATE TABLE IF NOT EXISTS budget as SELECT * FROM budget;
    """
    return query1


def query_inc(x):
    # income
    query3 = f"""
            SELECT SUM(amount) FROM transactions 
            WHERE Budget_Line = {x + 5}
        """
    return query3


def query_sumt(x):
    # Expenses
    query_sumt = f"""
            SELECT SUM(amount) FROM transactions 
            WHERE Budget_Line = {x}
        """
    return query_sumt


def query_sumb(x):
    query_sumb = f"""
        SELECT BUDGET FROM budget
        WHERE Budget_Line = {x}
    """
    return query_sumb
