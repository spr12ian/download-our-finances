from cls_helper_log import LogHelper
from cls_helper_sqlalchemy import SQLAlchemyHelper
from sqlalchemy.ext.declarative import declarative_base

# filepath: /home/probity/projects/download-our-finances/execute_sqls.py
from sqlalchemy import create_engine, text
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, t_bank_accounts as BankAccount, t_transactions as Transaction

Base = declarative_base()

# Replace with your actual database URL
DATABASE_URL = "sqlite:///our_finances.sqlite"

# Create an engine
engine = create_engine(DATABASE_URL)

queries = [
    [
        """
SELECT strftime('%Y-%m', t.Date) as month, 
SUM(Credit) as money_in, 
SUM(Debit) as money_out, 
SUM(Credit - Debit) as net_amount
FROM bank_accounts b 
JOIN transactions t ON b.key = t.key
WHERE "Our money" = "TRUE"
AND t.Description LIKE "X%"
GROUP BY month
ORDER BY month
    """
    ],
    """
SELECT t.key, SUM(Credit) as money_in, SUM(Debit) as money_out, SUM(Credit - Debit)
FROM bank_accounts b JOIN transactions t
ON b.key = t.key
WHERE "Our money"="TRUE"
AND t.Date BETWEEN "2025-01-01" AND "2025-01-31"
AND t.Description LIKE "X%"
GROUP BY t.key
    """,
]
# Execute the query
with engine.connect() as connection:
    for query in queries:
        print(query)
        result = connection.execute(text(query))
        for row in result:
            print(row)


from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, BankAccount, Transaction

# Replace with your actual database URL
DATABASE_URL = "sqlite:///your_database.db"

# Create an engine
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Perform the query
results = (
    session.query(
        func.strftime("%Y-%m", Transaction.Date).label("month"),
        func.sum(Transaction.Credit).label("money_in"),
        func.sum(Transaction.Debit).label("money_out"),
        func.sum(Transaction.Credit - Transaction.Debit).label("net_amount"),
    )
    .join(BankAccount, BankAccount.key == Transaction.key)
    .filter(
        Transaction.Our_money == True,
        Transaction.Description.like("X%"),
        Transaction.Date.between("2025-01-01", "2025-01-31"),
    )
    .group_by(func.strftime("%Y-%m", Transaction.Date))
    .order_by("month")
    .all()
)

# Print the results
for result in results:
    print(
        f"Month: {result.month}, Money In: {result.money_in}, Money Out: {result.money_out}, Net Amount: {result.net_amount}"
    )
