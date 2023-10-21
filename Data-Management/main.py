from terra.base_client import Terra

import uuid

terra = Terra(api_key='EEFXq0ofN_SJ5fg7hzOb2r02HIw5wtUZ', dev_id='drwatch-testing-a1uqRDmD1q', secret='secret')
api_responce = terra.list_providers()
parsed_responce = api_responce.get_parsed_response()
#print(parsed_responce)

user_id = str(uuid.uuid4())

widget_responce = terra.generate_widget_session(
    reference_id=user_id,
    providers=["APPLE", "GOOGLE", "GARMIN", "FITBIT"],
    auth_success_redirect_url="https://example.com/success",
    auth_failure_redirect_url="https://example.com/failure",
    language="en"
).get_parsed_response()

print(widget_responce)


