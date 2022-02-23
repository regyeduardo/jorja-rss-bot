"""Timezone module."""
import pytz


def get_timezone(timezone):
    """Return timezones."""
    try:
        return pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return False
