FROM mongo
COPY code/employees.json /employees.json
CMD mongoimport --db employees --collection employee --type json --file /employees.json --jsonArray