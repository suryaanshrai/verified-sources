# generated by datamodel-codegen:
#   filename:  specs.yml
#   timestamp: 2024-04-23T07:43:29+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class ConnectionSpecification(BaseModel):
    client_id: str = Field(
        ..., description='client id for the project', title='Client ID'
    )
    client_secret: str = Field(
        ..., description='client secret for the project', title='Client Secret'
    )
    refresh_token: str = Field(
        ..., description='refresh token for the project', title='Refresh Token'
    )


class GoogleDriveSpecification(BaseModel):
    class Config:
        extra = 'allow'

    name: Optional[str] = 'GoogleDrive'
    module_name: Optional[str] = 'google_drive'
    protocol_version: Optional[Any] = None
    documentation_url: Optional[str] = (
        'https://developers.google.com/drive/api/guides/about-sdk'
    )
    changelog_url: Optional[str] = 'www.example.com'
    connection_specification: ConnectionSpecification = Field(
        ...,
        description='ConnectorDefinition specific blob. Must be a valid JSON string.',
    )
