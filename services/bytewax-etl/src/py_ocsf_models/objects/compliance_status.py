from enum import IntEnum
from typing import Optional

from pydantic.v1 import BaseModel


class StatusID(IntEnum):
    """
    The normalized status identifier of the compliance check.

    0   Unknown: The status is unknown.
    1   Pass: The compliance check passed for all the evaluated resources.
    2   Warning: The compliance check did not yield a result due to missing information.
    3   Fail: The compliance check failed for at least one of the evaluated resources.
    99	Other: The event status is not mapped. See the status attribute, which contains a data source specific value.
    """

    Unknown = 0
    Pass = 1
    Warning = 2
    Fail = 3
    Other = 99


class ComplianceStatus(BaseModel):
    """
    The Compliance Status object contains information about the status of a compliance check or assessment.

    Attributes:
    - Status (status) [Optional]: The compliance status, as reported by the source.
    - Status ID (status_id) [Optional]: The normalized status identifier of the compliance check.
    """

    status: Optional[str]
    status_id: Optional[StatusID]
