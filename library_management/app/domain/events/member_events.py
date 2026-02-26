from app.infrastructure.kafka.producer import publish_event
from datetime import datetime

TOPIC = "member-events"


def member_created_event(member):
    event = {
        "event_type": "MEMBER_CREATED",
        "member_id": member["member_id"],
        "name": member["name"],
        "timestamp": datetime.utcnow().isoformat(),
                }

    publish_event(TOPIC, event)





def  member_updated_event(member):
    event = {
        "event_type": "MEMBER_UPDATED",
        "member_id": member["member_id"],
        "name": member["name"],
        "timestamp": datetime.utcnow().isoformat(), 
           
              }

    publish_event(TOPIC, event)



 
def member_deleted_event(member_id: int):
    event = {
        "event_type": "MEMBER_DELETED",
        "member_id": member_id,
        "timestamp": datetime.utcnow().isoformat(), 
    }

    publish_event(TOPIC, event)
