#!/bin/sh

export PGUSER="postgres"

# Check if database exists
DB_EXISTS=$(psql -tAc "SELECT 1 FROM pg_database WHERE datname='inventory'")

# Create database if it does not exist
if [ "$DB_EXISTS" != "1" ]; then
  psql -c "CREATE DATABASE inventory"
fi

# Create extension if it does not exist
psql inventory -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"
