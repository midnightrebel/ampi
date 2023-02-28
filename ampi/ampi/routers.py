class AMPIRouter:
    @classmethod
    def db_for_read(cls, model, **hints):
        if model._meta.app_label == 'files':
            return 'files'
        if model._meta.app_label == 'reports':
            return 'reports'
        return None

    @classmethod
    def db_for_write(cls, model, **hints):
        if model._meta.app_label == 'files':
            return 'files'
        if model._meta.app_label == 'reports':
            return 'reports'
        return None

    @classmethod
    def allow_relation(cls, obj1, obj2, **hints):
        return None

    @classmethod
    def allow_migrate(cls, db, app_label, model_name=None, **hints):
        if app_label == 'files':
            return db == 'files'
        if db == 'files':
            return False
        if app_label == 'reports':
            return db == 'reports'
        if db == 'reports':
            return False
        return None
