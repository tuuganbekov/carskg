import peewee
from decouple import config

db = peewee.PostgresqlDatabase(config('DB_NAME'), host=config('HOST'), port=config('PORT'),
                               user=config('DBUSER'), password=config('PASSWORD'))


class Car(peewee.Model):
    name = peewee.CharField(max_length=250)
    description = peewee.TextField()
    year = peewee.IntegerField()
    mileage = peewee.IntegerField()
    price_usd = peewee.IntegerField()
    image_link = peewee.TextField()
    link = peewee.TextField()

    class Meta:
        database = db
        db_table = 'cars'

db.create_tables([Car])
