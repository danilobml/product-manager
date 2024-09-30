#!/bin/sh

export PG_USER="postgres"

# create the database
psql -c "CREATE DATABASE inventory" 

# add the uuid extension
psql inventory -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"