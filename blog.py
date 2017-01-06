import os
from flask_script import Manager
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


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

    def __repr__(self):
        return "Entry %s" % self.title


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return "Tag %s" % self.name


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    manager.run()
