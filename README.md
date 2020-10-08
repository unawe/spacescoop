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
