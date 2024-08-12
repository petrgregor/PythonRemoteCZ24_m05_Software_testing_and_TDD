from collections import Counter
import re
def word_count(text: str) -> dict:
    """prevod textu na mala pismena"""
    text + text.lower()
    """pouziti regularniho vyrazu k extrakci slow"""
    words = re.findall(r'\b\w+\b', text)
    """pocitani vysky"""
