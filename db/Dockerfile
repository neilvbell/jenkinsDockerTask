# Derived from official mysql image (our base image)
# Use mysql 5.7 as the flask-app is not set up to work with later versions
FROM mysql:5.7

# Add a database and root password
# For hints on how to do this, consult the mysql 5.7 image documentation
ENV MYSQL_ROOT_PASSWORD="default_root"
ENV MYSQL_DATABASE="flask-db"
#ENV MYSQL_USER=user
#ENV MYSQL_PASSWORD=user_password

# Set the default user for the MySQL image
#USER mysql

# Expose port 3306 to allow connections to the database
EXPOSE 3306

# Add the content of the .sql file to your image
# All scripts copied to docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY CreateTable.sql /docker-entrypoint-initdb.d/