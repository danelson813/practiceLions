def query():
    query_ = """
        CREATE TABLE IF NOT EXISTS transactions AS SElECT * FROM ledger;
        """
    return query_


def query1():
    query1_ = """
        CREATE TABLE IF NOT EXISTS budget AS SELECT * FROM budget;
        """
    return query1_


def query_inc(x):
    # income
    query3_ = f"""
        SELECT SUM(amount) FROM transactions 
        WHERE Budget_Line = {x + 5}
        """
    return query3_


def query_sumt(x):
    # Expenses
    query_sumt_ = f"""
        SELECT SUM(amount) FROM transactions 
        WHERE Budget_Line = {x}
        """
    return query_sumt_


def query_sumb(x):
    query_sumb_ = f"""
        SELECT BUDGET FROM budget
        WHERE Budget_Line = {x}
        """
    return query_sumb_
