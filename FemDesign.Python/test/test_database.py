from pathlib import Path

from femdesign.io import deserialize_from_filepath, serialize_to_struxml
from femdesign.interop import *
import uuid
from xsdata.models.datatype import XmlDateTime
import pytest


def test_serialize_to_struxml_removes_namespace_prefixes() -> None:
	
	db = Database(
        # Required attributes
        struxml_version="24.00.003",
        source_software="FD Python API",
        start_time= XmlDateTime.now(),
        end_time= XmlDateTime.now(),
        guid= str(uuid.uuid4()),
        # Optional attributes with defaults
        standard=Standardtype.EC,
        country=Eurocodetype.COMMON,
        soil_as_solid=False,
        convertid="00000000-0000-0000-0000-000000000000",
        end =EmptyType(),
    )

	xml_content = serialize_to_struxml(db, pretty_print=False)

	assert xml_content.lstrip().startswith("<?xml")
	assert "urn:strusoft" in xml_content
	assert "ns0:" not in xml_content
	assert "xmlns:ns0=" not in xml_content
	assert 'xmlns:=""' not in xml_content


def test_deserialize_from_filepath_parses_database() -> None:
	asset_path = r"test/assets/concrete_beam.struxml"

	database = deserialize_from_filepath(str(asset_path))

	assert isinstance(database, Database)
	assert database.entities is not None
	assert len(database.entities.bar) > 0

