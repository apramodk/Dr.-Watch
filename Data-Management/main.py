from terra.base_client import Terra
from datetime import datetime, timedelta
import uuid
 
terra = Terra(
    api_key="EEFXq0ofN_SJ5fg7hzOb2r02HIw5wtUZ",
    dev_id="drwatch-testing-a1uqRDmD1q",
    secret="secret",
)

user_id = str(uuid.uuid4())
 
res = terra.generate_widget_session(
    providers=["GARMIN"],
    auth_success_redirect_url="https://example.com/success",
    auth_failure_redirect_url="https://example.com/failure",
    language="en",
    reference_id=user_id,
)


user_id_sample = user_id
user = terra.from_user_id(user_id_sample)
 
start_date = datetime.now() - timedelta(days=1)
end_date = datetime.now()
 
activity_response = terra.get_activity_for_user(user, start_date, end_date, to_webhook=False)
parsed_activities = activity_response.parsed_response
 
print(parsed_activities)

print(res.json['url'])