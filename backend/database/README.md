# PostgreSQL Database

This project uses PostgreSQL as the database server.

This folder contains files pertaining to the starting the database (`schema.sql`), and the structure of the database schema (`RelationalModelvX.drawio`).

## Starting a Local Database Server via Command Line

Assuming you've got Postgres installed locally, start a `psql` shell. Typically this is as simple as running the command `psql` on whatever terminal you have. Note: you might have to add it to your PATH.

In the `psql` shell, you can list whatever databases your server has running with `\l`. Connect to a database you want to use build the schema in with `\c <database_name>`, or create a database with `CREATE DATABASE <database_name>;` then connect to it, again with the `\c <database_name>` command.

Finally, to run the `schema.sql` script. Do this by running `\i <abs_path_to_schema.sql>`.

The database should now have the all tables and relations as per `schema.sql`.
