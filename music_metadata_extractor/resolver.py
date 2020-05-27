import re
from enum import Enum
from typing import Tuple
from .sources import get_yt_info
from .models import BaseProviderInput


class SupportedSources(Enum):
    """Enum to track supported input link platforms"""

    youtube = 1


def _is_youtube(input_url: str) -> bool:
    """Verify if input url is a valid YouTube link"""
    if bool(
        re.match(
            r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?",
            input_url,
        )
    ):
        return True
    return False


def _resolve_link(input_url: str) -> SupportedSources:
    """Resolve the input link platform"""
    if _is_youtube(input_url):
        return SupportedSources.youtube
    raise ValueError("Unsupported URL!")


def get_source_data(input_url: str) -> Tuple[BaseProviderInput, dict]:
    """Get input object required by providers to fetch metadata"""
    source_type = _resolve_link(input_url)
    if source_type == SupportedSources.youtube:
        provider_input, extraAttrs = get_yt_info(input_url)
    else:
        raise ValueError("Unsupported URL!")
    return provider_input, extraAttrs
