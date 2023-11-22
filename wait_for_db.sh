#!/bin/sh

# wait_for_db script

echo "Waiting for PostgreSQL to start..."

while ! nmap -p 5432 -T5 -sT db | grep -q "5432/tcp open"; do
  sleep 1
done

echo "PostgreSQL started"