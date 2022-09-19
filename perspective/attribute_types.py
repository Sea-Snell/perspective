# from typing import Dict, List, Literal, Optional, Union
from typing import Any

COMMENT_TYPE = Any # Optional[Literal['PLAIN_TEXT', 'HTML']]
CONTEXT = Any # Optional[List[Dict[Literal["text", "type"], str]]]
REQUESTED_ATTRIBUTES = Any # Optional[Dict[str, Dict[Literal["scoreType", "scoreThreshold"], Union[str, float]]]]
LANGUAGES = Any # Optional[List[str]]
SUMMARY_SCORE = Any # Union[Dict[Literal["value"], float], Dict[Literal["type"], str]]
SPAN_SCORE_POSITION = Any # Dict[Literal["begin", "end"], int]
SPAN_SCORE_VALUE = Any # Dict[Literal["score"], Union[Dict[Literal["value"], float], Dict[Literal["type"], str]]]
SPAN_SCORES = Any # List[Union[SPAN_SCORE_POSITION, SPAN_SCORE_VALUE]]
ATTRIBUTE_SCORES = Any # Dict[str, Union[SUMMARY_SCORE, SPAN_SCORES]]
