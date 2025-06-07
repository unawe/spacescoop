# Migration instructions

To import a dumpfile from the old Space Scoop website

```
dropdb   -U postgres --if-exists  spacescoop
createdb -U postgres -T template0 spacescoop
pg_restore -U postgres -d spacescoop <PATH TO DUMP FILE>

# From spacescoop-old
python manage.py dumpdata -e sessions  --natural-foreign --natural-primary -e taggit | gzip > fullsite.json.gz
mv fullsite.json.gz ../spacescoop/


# From Divio version
docker-compose run web python manage.py loaddata fullsite.json.gz -e taggit
```

The site is hosted on the Divio cloud. To deploy use [the Divio Deploying Django tutorial](https://docs.divio.com/en/latest/introduction/django-02-create-project/) as a reference.

# Railway deployment

To migrate from the Divio Cloud

Need to create the Divio database user

```
createuser -s spacescoop-live-8e5e7e124f284780baf074fb522c258b-a560e1d  -U postgres --host=autorack.proxy.rlwy.net --port=10577
```

If the DB has been reployed you may need to change host and port

Download the database dump file from Divio cloud

Then use `pg_restore` to import the database

```
pg_restore -c --if-exists -U postgres -d railway -1 spacescoop.dump --host=autorack.proxy.rlwy.net --port=10577
```

## Apply migrations

From the local directory, you need to run any commands to sync the current code base and database ie.

```
railway run python manage.py migrate
```

This will only work if you have the `public` hostname for the database in the settings