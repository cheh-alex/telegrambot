from peewee import SqliteDatabase,CharField,IntegerField,Model

connection = SqliteDatabase('History.db')

class Query(Model):

    chat_id = CharField(max_length=100,null=False)
    type = CharField(max_length=20,null=False)
    category = CharField(max_length=100)
    amount = IntegerField()

    class Meta:
        database = connection
        db_table = 'queries'

Query.create_table()