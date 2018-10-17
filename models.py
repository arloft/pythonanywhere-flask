# import from peewee
from peewee import *

# connect to the SQLite database, in the "db-files" folder
db = SqliteDatabase('/home/arloft/learn/edhdecks.db')
# ^ pythonanywhere requires the full path to the .db file

# define what a 'Deck' is
class Deck(Model):
    # these are all the fields it has
    # match up TextField/IntegerField/etc with correct type
    # see link for list of field types: http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table
    dbn = IntegerField(primary_key=True) # primary key = unique id
    deck_name = TextField()
    deck_color = TextField()
    deck_cmc = FloatField()
    deck_creature = IntegerField()
    deck_artifact = IntegerField()
    deck_enchantment = IntegerField()
    deck_sorcery = IntegerField()
    deck_instant = IntegerField()
    deck_planeswalker = IntegerField()
    deck_land = IntegerField()

    class Meta:
        # data is coming from edhdecks.db
        database = db
        # and it's in the table called 'py-edh-deck-list'
        db_table = 'py-edh-deck-list'

# repeat with the Performance Stats data
class Score(Model):
    dbn = IntegerField(primary_key=True)
    deck_name = TextField()
    deck_winloss = TextField()
    game_turncount = IntegerField()
    opp1_deck = TextField()
    opp1_deck_colors = TextField()
    opp2_deck = TextField()
    opp2_deck_colors = TextField()
    opp3_deck = TextField()
    opp3_deck_colors = TextField()
    opp4_deck = TextField()
    opp4_deck_colors = TextField()

    class Meta:
        database = db
        db_table = 'py-edh-deck-performance-stats'