from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Import the Base class to inherit from
from database import Base

# Define the Legend model, representing the 'legends' table
class Legend(Base):
    __tablename__ = "legends"  # Name of the table in the database

    # Define the columns of the table
    id = Column(Integer, primary_key=True, index=True)  # Primary key with an index
    name = Column(String(150), nullable=False)  # Legend's name, required
    description = Column(String(500))  # Optional description of the legend
    legend_type_id = Column(Integer, ForeignKey("legend_types.id"))  # Foreign key to legend_types table

    # Define the relationship between Legend and LegendType
    legend_type = relationship("LegendType", back_populates="legends")
