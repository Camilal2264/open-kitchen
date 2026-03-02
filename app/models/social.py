"""Social interaction models."""
from app.db import get_db


class Review:
    """Review model."""
    
    @staticmethod
    def get_by_recipe(recipe_id):
        """Get all reviews for a recipe."""
        db = get_db()
        return db.execute(
            'SELECT r.*, u.username FROM reviews r '
            'JOIN users u ON r.user_id = u.id '
            'WHERE r.recipe_id = ? ORDER BY r.created_at DESC',
            (recipe_id,)
        ).fetchall()


class Comment:
    """Comment model."""
    
    @staticmethod
    def get_by_recipe(recipe_id):
        """Get all comments for a recipe."""
        db = get_db()
        return db.execute(
            'SELECT c.*, u.username FROM comments c '
            'JOIN users u ON c.user_id = u.id '
            'WHERE c.recipe_id = ? ORDER BY c.created_at DESC',
            (recipe_id,)
        ).fetchall()


class SavedRecipe:
    """Saved recipe model."""
    
    @staticmethod
    def get_by_user(user_id):
        """Get all saved recipes for a user."""
        db = get_db()
        return db.execute(
            'SELECT r.*, u.username as author_name, sr.saved_at '
            'FROM saved_recipes sr '
            'JOIN recipes r ON sr.recipe_id = r.id '
            'JOIN users u ON r.author_id = u.id '
            'WHERE sr.user_id = ? '
            'ORDER BY sr.saved_at DESC',
            (user_id,)
        ).fetchall()
