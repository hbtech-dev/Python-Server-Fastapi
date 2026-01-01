from sqlalchemy.orm import Session
from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.core.security import get_password_hash


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
    
    user = db.query(User).filter(User.email == "admin@example.com").first()
    if not user:
        user = User(
            email="admin@example.com",
            username="admin",
            hashed_password=get_password_hash("admin123"),
            full_name="Admin User",
            is_active=True,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
