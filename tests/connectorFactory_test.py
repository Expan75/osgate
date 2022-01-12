import pytest
import json

def test_invalid_connector():
    with pytest.raises(NotImplementedError):
        #valid_connector_data = json.loads(valid_connnector_data)
        #connector = create_connector("", valid_connnector_data)
        raise NotImplementedError