from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    owner = relationship("User", back_populates="items")
