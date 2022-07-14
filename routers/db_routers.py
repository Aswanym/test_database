from decouple import config

class OrderRouter:
    route_app_labels = {'auth', 'contenttypes', 'admin', 'sessions', 'messages', 'staticfiles', 'order'}
    """
    A router to control all database operations on models in the
    order application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read order models go to order_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'order_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'order_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label in self.route_app_labels or \
           obj2._meta.app_label in self.route_app_labels:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label in self.route_app_labels:
            return db == 'order_db'
        return None


class ProductRouter:
    route_app_labels = {'auth', 'contenttypes', 'admin', 'sessions', 'messages', 'staticfiles', 'product'}
    """
    A router to control all database operations on models in the
    order application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read order models go to order_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'product_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'product_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label in self.route_app_labels or \
           obj2._meta.app_label in self.route_app_labels:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label in self.route_app_labels:
            return db == 'product_db'
        return None