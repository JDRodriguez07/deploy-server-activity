# Load environment variables from the .env file for MySQL database connection
load_dotenv()

# Read environment variables for database credentials and parameters
DB_USERNAME = os.getenv("username")
DB_PASSWORD = os.getenv("password")
DB_DATABASE = os.getenv("database")
DB_HOST = "mysql"  # This will be the service name in docker-compose
DB_PORT = "3306"

# Build the database connection URL using the environment variables
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# Create the SQLAlchemy engine to interact with the MySQL database
engine = create_engine(DATABASE_URL)

# Create the SQLAlchemy session to manage transactions and communicate with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the declarative base class that will be used to define the database tables
Base = declarative_base()
