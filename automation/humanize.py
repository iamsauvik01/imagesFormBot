import random
import time

def human_delay(min_s=0.3, max_s=1.2):
    """Random delay between actions"""
    time.sleep(random.uniform(min_s, max_s))


def human_type(page, selector, text):
    """Type like a human, character by character"""
    for char in str(text):
        page.type(selector, char, delay=random.randint(50, 140))


def human_click(page, selector):
    """Click with a slight delay"""
    human_delay(0.4, 0.9)
    page.click(selector)


def human_select(locator):
    """Pause after dropdown select"""
    human_delay(0.8, 1.5)
