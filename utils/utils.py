import model
from languages import LANGUAGES as lang



def ab_language(language_name: str) -> str:
    """
    Get abbreviation of a language name.

    Parameters
    ----------
    language_name : str
        Full language name.

    Returns
    -------
    str
        Abbreviation if found, else None.
    """
    for abbr, name in lang.items():
        if name.lower() == language_name.lower():
            return abbr
    return None 


def calling(text, in_lang, out_lang):
    """
    Translate text using model.

    Parameters
    ----------
    text : str
        Input text to translate.
    in_lang : str
        Source language abbreviation.
    out_lang : str
        Target language abbreviation.

    Returns
    -------
    str
        Translated text.
    """
    translation = model.translate(text, in_lang="en", out_lang="es")

    return translation