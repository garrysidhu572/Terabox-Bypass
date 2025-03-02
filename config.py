import os
import logging
import re
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

my_cookie = os.environ.get("MY_COOKIES")
my_headers = os.environ.get("MY_HEADERS")
session_string = os.environ.get("session_string")
allowed_groups = os.environ.get("allowed_groups") or "-1002074421298"  # added random group id to avoid NoneType error
# allowed_groups = ["-1002074421298"] or ["-1002074421298", "-1002074421298"]
owner_id = os.environ.get("owner_id") or "1718738592"

try:
    my_cookie = eval(my_cookie)
    my_headers = eval(my_headers)
    allowed_groups = eval(allowed_groups)
except Exception as e:
    logger.error(f"Error parsing env variables: {e}")


def extract_links(message):
    # fetch all links
    try:
        url_pattern = r'https?://\S+'
        matches = re.findall(url_pattern, message)

        return matches
    except Exception as e:
        logger.error(f"Error extracting links: {e}")
        return []
