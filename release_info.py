import argparse
from pymongo import MongoClient
from datetime import datetime

def insert_release_info(user, service_name, release_tag, mongo_user, mongo_password):
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@localhost:27017")
    db = client.sj_release
    collection = db.audit_log

    try:
        document = {
            "msg": f"{user} deployed service {service_name}:{release_tag}",
            "time": datetime.utcnow().isoformat()
        }
        result = collection.insert_one(document)
        print(f"Document inserted with ID: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Insert a release info document into MongoDB")
    parser.add_argument("--user", required=True, help="Username of the person deploying the service")
    parser.add_argument("--service_name", required=True, help="Name of the service being deployed")
    parser.add_argument("--release_tag", required=True, help="Release tag of the deployment")
    parser.add_argument("--mongo_user", required=True, help="MongoDB username")
    parser.add_argument("--mongo_password", required=True, help="MongoDB password")

    args = parser.parse_args()
    insert_release_info(args.user, args.service_name, args.release_tag, args.mongo_user, args.mongo_password)