from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Legend(Base):
    __tablename__ = "legends"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(500))
    legend_type_id = Column(Integer, ForeignKey("legend_types.id"))

    legend_type = relationship("LegendType", back_populates="legends")