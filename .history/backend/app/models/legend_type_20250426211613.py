
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Import the Base class to inherit from
from database import Base

# Define the LegendType model, representing the 'legend_types' table
class LegendType(Base):
    __tablename__ = "legend_types"  # Name of the table in the database

    # Define the columns of the table
    id = Column(Integer, primary_key=True, index=True)  # Primary key with an index
    name = Column(String(100), nullable=False)  # Type name, required

    # Define the relationship with the Legend model
    legends = relationship("Legend", back_populates="legend_type")
