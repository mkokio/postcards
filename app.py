from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///totorotuesday.db'
app.config['IMAGE_FOLDER'] = '/static/images'
db = SQLAlchemy(app)

from db.models import Tag, TotoroTuesday

@app.route("/")
def index():
    tags = Tag.query.all()
    totorotuesday= TotoroTuesday.query.all()
    return render_template("index.html", tags=tags, totorotuesday=totorotuesday)

@app.route('/filter_images', methods=['POST'])
def filter_images():
    selected_tags = request.form.getlist('tags[]')
    # Filter images based on selected tags
    filtered_images = TotoroTuesday.query.join(TotoroTuesday.tags).filter(Tag.id.in_(selected_tags)).all()
    # Return filtered images as JSON response
    return jsonify({'images': [image.name for image in filtered_images]})


if __name__ == '__main__':
    app.run(debug=True)