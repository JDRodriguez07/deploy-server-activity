from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class LegendType(Base):
    __tablename__ = "legend_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    legends = relationship("Legend", back_populates="legend_type")
