from . import app, basic_auth, db
from .models import Tag, Entry
from flask import render_template, request, redirect, url_for
from .forms import ArticleForm, TagForm 


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret', methods=('GET',))
@basic_auth.required
def admin_main():
    e = Entry.query.all()
    return render_template('admin_main.html', entries=e)


@app.route('/secret/add_post', methods=('GET', 'POST'))
@basic_auth.required
def add_new_article():
    if request.method == 'POST':
        tags = []
        for tag in request.form.getlist('tags'):
            tag_object = Tag.query.filter_by(name=tag).first()
            tags.append(tag_object)
        
        new_article = Entry(title=request.form['title'],
                            content=request.form['content'],
                            tags=tags)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('admin_main'))
    else:
        form = ArticleForm()
        form.tags.choices =[(t, t) for t in Tag.query.all()]
        return render_template('add_post.html', form=form)


@app.route('/secret/add_tag', methods=('GET','POST'))
@basic_auth.required
def add_new_tag():
    if request.method == 'POST':
        new_tag = Tag(name=request.form['name'])
        db.session.add(new_tag)
        db.session.commit()
        return redirect(url_for('admin_main'))
    else:
        form = TagForm()
        return render_template('add_tag.html', form=form)

@app.route('/secret/<slug>', methods=('GET', 'POST'))
@basic_auth.required
def edit_article(slug):
    return slug


