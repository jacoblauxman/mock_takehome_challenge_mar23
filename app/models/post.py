from .db import db, environment, SCHEMA, add_prefix_for_prod, TimestampMixin
from sqlalchemy.orm import relationship, declarative_mixin
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Numeric


class Post(db.Model, TimestampMixin):
  __tablename__ = 'posts'

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String(255), nullable=False)
  text = Column(String(2000), nullable=False)
  rating = Column(Integer, nullable=False)
  coffee_id = Column(Integer, ForeignKey(add_prefix_for_prod("coffees.id")), nullable=False)

  coffee = relationship("Coffee", back_populates="posts")

  def to_dict(self):
      return {
          "id": self.id,
          "title": self.title,
          "text": self.text,
          "rating": self.rating,
          "coffeeId": self.coffee_id,
          "createdAt": self.created_at,
          "updatedAt": self.updated_at,

          "coffee": self.coffee.to_dict()
      }
