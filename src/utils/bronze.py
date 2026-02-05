# Utilization responsible for bronze-specific row preparation
# Each row contains raw_json, ingested_at, source, batch_id
# Import libraries
from typing import List, Dict, Tuple
from datetime import datetime
import json
import uuid

# Prepare bronze rows
def prepare_bronze_rows(
    records: List[Dict],
    source: str
) -> List[Tuple[str, datetime, str, str]]:
    """
    Convert raw records into bronze-compatible rows.
    Each row contains:
    - raw_json
    - ingested_at
    - source
    - batch_id
    """
    batch_id = str(uuid.uuid4()) # Give each batch a unique ID
    ingested_at = datetime.utcnow() # Capture ingestion time

    return [
        (
            json.dumps(record),
            ingested_at,
            source,
            batch_id
        )
        for record in records
    ]
