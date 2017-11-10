"""Model for learning journal entries."""

from sqlalchemy import (
    Column,
    Date,
    Integer,
    Text,
)

from .meta import Base


class Entry(Base):
    """Entry model class."""

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    created = Column(Date)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created': self.created.strftime('%Y-%m-%d')
        }
