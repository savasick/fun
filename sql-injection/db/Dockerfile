FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=user
ENV POSTGRES_DB=test
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql