# generated by datamodel-codegen:
#   filename:  catalog.yml
#   timestamp: 2024-08-07T14:27:34+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import Field
from dat_core.pydantic_models import DatDocumentStream, DatCatalog

class FileType(Enum):
    pdf = 'pdf'
    txt = 'txt'
    csv = 'csv'
    html = 'html'
    md = 'md'
    log = 'log'


class DocumentStream(DatDocumentStream):
    name: Optional[str] = Field(
        'document_stream',
        description='The name of the document stream.',
        json_schema_extra={
            'ui-opts': {
                'hidden': True,
            }
        }
    )
    namespace: Optional[str] = Field(
        None, description='namespace the data is associated with'
    )
    file_name: str = Field(...,
                           description='Name Of The File', title='File Name')
    folder_path: str = Field(..., title='Directory Paths')
    file_type: FileType = Field(..., title='Type of File')


class GoogleCloudStorageCatalog(DatCatalog):
    document_streams: List[DocumentStream] = None
