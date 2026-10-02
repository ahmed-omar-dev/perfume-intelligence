class PerfumeAppError(Exception):
    """Base exception for the perfume application."""
    pass


class PerfumeNotFoundError(PerfumeAppError):
    """Raised when a perfume cannot be found."""
    pass


class DuplicatePerfumeError(PerfumeAppError):
    """Raised when a perfume already exists."""
    pass


class InvalidPriceError(PerfumeAppError):
    """Raised when a perfume price is invalid."""
    pass


class InvalidRatingError(PerfumeAppError):
    """Raised when a perfume rating is invalid."""
    pass


class InvalidStockError(PerfumeAppError):
    """Raised when perfume stock is invalid."""
    pass


class InvalidScoreError(PerfumeAppError):
    """Raised when longevity or sillage score is invalid."""
    pass