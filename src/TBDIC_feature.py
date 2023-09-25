def feature_enabled(func):
    """
    This decorator checks whether a feature is enabled or not.
    """

    FEATURE_STATUS = {
        '_applyRoundedCorners': False,
        '_imageLoader': False,
        'rounded_corners_feature_supported': False
    }

    def wrapper(self, *args, **kwargs):
        if FEATURE_STATUS[func.__name__]:
            return func(self, *args, **kwargs)
        else:
            return None
    return wrapper
