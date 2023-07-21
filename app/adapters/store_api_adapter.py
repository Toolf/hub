import logging
import requests
from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway


class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_data: ProcessedAgentData):
        """
        Save the processed road data to the Store API.

        Parameters:
            processed_data (dict): Processed road data to be saved.

        Returns:
            bool: True if the data is successfully saved, False otherwise.
        """
        # Make a POST request to the Store API endpoint with the processed data
        endpoint_url = f"{self.api_base_url}/agent_data"
        try:
            response = requests.post(endpoint_url, json=processed_data.model_dump())

            if response.status_code == 201:
                logging.info("Processed road data saved successfully.")
                return True
            else:
                logging.info(
                    f"Failed to save processed road data. Status code: {response.status_code}"
                )
                return False

        except requests.exceptions.RequestException as e:
            logging.info(f"Failed to connect to the Store API: {e}")
            return False
