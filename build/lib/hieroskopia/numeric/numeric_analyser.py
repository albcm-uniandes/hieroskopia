from pandas import Series
from ..utils.evaluator import Evaluator


class NumericAnalyser(object):
    """
    Receive a column and try to analyze  the three digit separator,
    the decimal separator and get the numeric format pattern
    using regexp
    Return a dict with key named 'format'
    with the pandas patterns
    """
    @staticmethod
    def numeric_format_matcher(series: Series):
        # Identify stage
        numeric_dict = {
            # -1234 or -1234.12
            "^[-]?[\\d]+[.]?\\d+": {
                'three_digit_separator': '',
                'decimal_separator': '.'
            },
            # -12,345.1234
            "^[-]?\\d{1,3}(,\\d{3})*(\\.\\d+)?$": {
                'three_digit_separator': ',',
                'decimal_separator': '.'
            }
        }

        simple_int_pattern = "\\d+"
        numeric_format = {
            'decimal_separator': '',
            'three_digit_separator': ''
        }
        if series.astype(str).str.match(simple_int_pattern).eq(True).all():
            # Todo: Find  generic pattern or -? \p{Sc} or \p{Sc} -?  to identify currencies
            # Todo if true then loop dict
            return numeric_format

        return numeric_format

