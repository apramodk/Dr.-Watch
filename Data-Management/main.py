from terra.base_client import Terra

from flask import Flask


import uuid

terra = Terra(api_key='EEFXq0ofN_SJ5fg7hzOb2r02HIw5wtUZ', dev_id='drwatch-testing-a1uqRDmD1q', secret='secret')
api_responce = terra.list_providers()
parsed_responce = api_responce.get_parsed_response()
#print(parsed_responce)

reference_id = str(uuid.uuid4())

widget_responce = terra.generate_widget_session(
    reference_id=reference_id,
    providers=["APPLE", "GOOGLE", "GARMIN", "FITBIT"],
    show_disconnect=True,
    language="en"
)

terraModel = terraModel()
print(widget_responce)


