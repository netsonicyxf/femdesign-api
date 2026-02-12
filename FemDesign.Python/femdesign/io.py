from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Tuple
import uuid

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from femdesign.interop import Database

def serialize_to_struxml(database: Database, pretty_print: bool = True, filepath: str | None = None) -> str:
    """
    Serialize the database to StruXML without namespace prefixes.
    
    Args:
        database: The Database object to serialize
        pretty_print: Whether to format the XML with indentation
        filepath: Optional file path to write the XML content to
    
    Returns:
        StruXML string representation
    """
    # Configure serializer
    config = SerializerConfig(
        pretty_print=pretty_print,
        xml_declaration=True,
        encoding="utf-8"
    )

    serializer = XmlSerializer(config=config)

    # Use empty string as prefix to remove ns0:
    ns_map = {"urn:strusoft": ""}

    xml_content = serializer.render(database, ns_map=ns_map)

    # Post-process to clean up any remaining namespace artifacts
    # Replace xmlns:="" with xmlns="" and remove empty namespace prefixes
    xml_content = xml_content.replace('xmlns:=""', 'xmlns=""')
    xml_content = xml_content.replace('ns0:', '')
    xml_content = xml_content.replace('xmlns:ns0=', 'xmlns=')

    # Write to file if filepath is provided
    if filepath:
        file_path = Path(filepath)
        # Create parent directories if they don't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(xml_content, encoding='utf-8')

    return xml_content


def deserialize_from_filepath(file_path: str) -> Database:
    parser = XmlParser()
    return parser.parse(file_path, Database)