import os
from flask_script import Manager
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from wtforms import Form, StringField, TextAreaField, SelectMultipleField, validators
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
manager = Manager(app)
bootstrap = Bootstrap(app)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'
basic_auth = BasicAuth(app)

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


class AdminForm(Form):
    title = StringField("Title", [validators.DataRequired("Please Enter your birthdate")])
    content = TextAreaField("Content", [validators.DataRequired("Please Enter your birthdate")])
    tags = SelectMultipleField("Tags", choices=[])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret', methods=('GET',))
@basic_auth.required
def admin_main():
    e = Entry.query.all()
    return render_template('admin_main.html', entries=e)


@app.route('/secret/add', methods=('GET', 'POST'))
@basic_auth.required
def add_new_article():
    form = AdminForm()
    form.tags.choices =[(t, t) for t in Tag.query.all()]

    # import ipdb
    # ipdb.set_trace()
    return render_template('admin.html', form=form)


@app.route('/secret/<slug>', methods=('GET', 'POST'))
@basic_auth.required
def edit_article(slug):
    return slug


if __name__ == '__main__':
    manager.run()

