from django.db import connection


def NO_CTE_SUPPORT():
    # This has to be as function because when it's a var it evaluates before
    # db is connected and we get OperationalError. MySQL version is retrived
    # from db, and it's cached_property.
    return (
        connection.vendor == 'sqlite' and
        connection.Database.sqlite_version_info < (3, 8, 3)
    ) or (
        connection.vendor == 'mysql' and
        connection.mysql_version < (8, 0)
    )
