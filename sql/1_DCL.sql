CREATE USER 'testuser'@'localhost' IDENTIFIED BY '1111';

GRANT ALL PRIVILEGES ON world.* TO 'testuser'@'localhost';

SHOW GRANTS FOR 'testuser'@'localhost';

revoke ALL PRIVILEGES ON world.* from 'testuser'@'localhost';

create role testrole;

grant all privileges on world.* to testrole;

grant testrole to 'testuser'@'localhost';

show grants for 'testuser'@'localhost';

revoke testrole from 'testuser'@'localhost';