class DatabaseRouter:
    """
    A router to control database operations for different apps.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'chatbot' or model._meta.app_label == 'chatbotapp':
            return 'chatbot'  # Use SQLite for chatbot app
        return 'default'  # Use MySQL for everything else

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'chatbot' or model._meta.app_label == 'chatbotapp':
            return 'chatbot'  # Use SQLite for chatbot app
        return 'default'  # Use MySQL for everything else

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations only within the same database
        db_set = {'default', 'chatbot'}
        if {obj1._state.db, obj2._state.db}.issubset(db_set):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'chatbot' or app_label == 'chatbotapp':
            return db == 'chatbot'
        return db == 'default'
