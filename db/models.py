from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app import db

# The model will generate a table name by converting the CamelCase class name to snake_case.

class Tag(db.Model):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class TotoroTuesday(db.Model):
    __tablename__ = 'totorotuesday'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tags = relationship("Tag", secondary="totorotuesday_tags", backref="tags")

class TotoroTuesdayTag(db.Model):
    __tablename__ = 'totorotuesday_tags'
    totoro_id = Column(Integer, ForeignKey('totorotuesday.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)