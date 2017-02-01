from . import db
from slugify import slugify
from datetime import datetime

entriestags = db.Table('entriestags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('entry_id', db.Integer, db.ForeignKey('entries.id'))
)


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text, unique=True)
    timestamp = db.Column(db.DateTime)
    tags = db.relationship('Tag', secondary=entriestags,
    backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(
                kwargs.get('title'),
                separator='_')
        
        if not 'timestamp' in kwargs:
            kwargs['timestamp'] = datetime.utcnow()    
        
        super(Entry, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return "Entry %s" % self.title


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return "%s" % self.name


