import re
from enum import Enum
from .sources import get_yt_info
from .models import BaseProviderInput


class SupportedSources(Enum):
    youtube = 1


def _is_youtube(input_url: str) -> bool:
    if bool(
        re.match(
            r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?",
            input_url,
        )
    ):
        return True
    return False


def _resolve_link(input_url: str) -> SupportedSources:
    if _is_youtube(input_url):
        return SupportedSources.youtube
    raise TypeError("Unsupported URL!")


def get_provider_input(input_url: str) -> BaseProviderInput:
    source_type = _resolve_link(input_url)
    if source_type == SupportedSources.youtube:
        provider_input = get_yt_info(input_url)
    else:
        raise TypeError("Unsupported URL!")
    return provider_input
