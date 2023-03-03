from .db import db, environment, SCHEMA, add_prefix_for_prod, TimestampMixin
from sqlalchemy.orm import relationship, declarative_mixin
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Numeric

class Coffee(db.Model, TimestampMixin):
  __tablename__ = 'coffees'

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = Column(Integer, primary_key=True, nullable=False)
  name = Column(String(255), nullable=False)
  year = Column(Integer, nullable=False)
  caffeine_content = Column(Numeric(precision=4, scale=2), nullable=False)
  caffeine_percentage = Column(Numeric(precision=4, scale=2), nullable=False)

  posts = relationship("Post", back_populates="coffee")

  def to_dict(self):
      return {
          "id": self.id,
          "name": self.name,
          "year": self.year,
          "caffeineContent": self.caffeine_content,
          "caffeinePercentage": self.caffeine_percentage,
          "createdAt": self.created_at,
          "updatedAt": self.updated_at,

          "posts": [post.to_dict() for post in self.posts]
      }
