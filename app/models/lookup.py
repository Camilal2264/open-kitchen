"""Lookup table models."""
from app.db import get_db


class Unit:
    """Unit model."""
    
    @staticmethod
    def get_all():
        """Get all units."""
        db = get_db()
        return db.execute('SELECT * FROM units ORDER BY name').fetchall()
    
    @staticmethod
    def create(name, abbreviation=None):
        """Create a new unit."""
        db = get_db()
        db.execute(
            'INSERT INTO units (name, abbreviation) VALUES (?, ?)',
            (name, abbreviation)
        )
        db.commit()


class Category:
    """Category model."""
    
    @staticmethod
    def get_all():
        """Get all categories."""
        db = get_db()
        return db.execute('SELECT * FROM categories ORDER BY name').fetchall()


class Tag:
    """Tag model."""
    
    @staticmethod
    def get_all():
        """Get all tags."""
        db = get_db()
        return db.execute('SELECT * FROM tags ORDER BY name').fetchall()


class Allergen:
    """Allergen model."""
    
    @staticmethod
    def get_all():
        """Get all allergens."""
        db = get_db()
        return db.execute('SELECT * FROM allergens ORDER BY name').fetchall()
