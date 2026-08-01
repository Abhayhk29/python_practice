<!-- Alembic command -->

alembic init <folder name>  Initialize a new, generic Environment
alembic revision -m <message>  create a new version of the environment
alembic upgrade <revison #> Run our upgrade to our database
alembic downgrade -1 Run our downgrade migration to our database



alembic.ini 
alembic directory 


python -m alembic init alembic(we can name as per our requirement)