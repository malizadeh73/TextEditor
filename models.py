import peewee

myDB = peewee.MySQLDatabase("text_editor_db", host="127.0.0.1", port=3306, user="root", passwd="", charset='utf8')


class MySQLModel(peewee.Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = myDB


class User(MySQLModel):
    id = peewee.PrimaryKeyField()
    email = peewee.CharField()
    token = peewee.IntegerField()
    date = peewee.DateField()
    counter = peewee.IntegerField()
