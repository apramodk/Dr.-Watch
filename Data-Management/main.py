from terra.base_client import Terra
import uuid
import datetime


terra = Terra(api_key='EEFXq0ofN_SJ5fg7hzOb2r02HIw5wtUZ', dev_id='drwatch-testing-a1uqRDmD1q', secret='secret')

reference_id = str(uuid.uuid4())
terra_user = terra.from_user_id(reference_id)

widget_responce = terra.generate_widget_session(
    reference_id=reference_id,
    providers=["GARMIN"],
    show_disconnect=True,
    language="en"
)

nutrition_resp = terra_user.get_nutrition(start_date=datetime.strptime('2023-03-29','%Y-%m-%d'), end_date=datetime.now(), to_webhook = False )
nutrition_resp_json = nutrition_resp.get_json()
print(nutrition_resp_json)

print(widget_responce.get_parsed_response())


