#!/bin/python
import json
import redis
from glossary.models import Glossary
from users.models import User


redis_server_host = "localhost"
redis_server_port = 6379
tmx_redis_db = 3
utm_redis_db = 6
redis_client = None
utm_redis_client = None
mongo_client_tmx = None
mongo_client_suggestion = None


class TMXRepository:
    def __init__(self):
        pass

    # Initialises and fetches redis client
    def redis_instantiate(self):
        global redis_client
        redis_client = redis.Redis(
            host=redis_server_host, port=redis_server_port, db=tmx_redis_db
        )
        return redis_client

    def utm_redis_instantiate(self):
        global utm_redis_client
        utm_redis_client = redis.Redis(
            host=redis_server_host, port=redis_server_port, db=utm_redis_db
        )
        return utm_redis_client

    def get_utm_redis_instance(self):
        global utm_redis_client
        if not utm_redis_client:
            return self.utm_redis_instantiate()
        else:
            return utm_redis_client

    def get_redis_instance(self):
        global redis_client
        if not redis_client:
            return self.redis_instantiate()
        else:
            return redis_client

    def upsert(self, key, value):
        try:
            client = self.get_redis_instance()
            # log_info(f"Key to TMX DB: {key}",None)
            # log_info(f"Value to TMX DB: {value}",None)
            client.set(key, json.dumps(value))
            return 1
        except Exception as e:
            log_exception("Exception in TMXREPO: upsert | Cause: " + str(e), None, e)
            return None

    def delete(self, keys):
        try:
            client = self.get_redis_instance()
            client.delete(*keys)
            return 1
        except Exception as e:
            log_exception("Exception in TMXREPO: delete | Cause: " + str(e), None, e)
            return None

    def search(self, key_list):
        try:
            client = self.get_redis_instance()
            result = []
            for key in key_list:
                val = client.get(key)
                if val:
                    result.append(json.loads(val))
            return result
        except Exception as e:
            log_exception("Exception in TMXREPO: search | Cause: " + str(e), None, e)
            return None

    def get_all_records(self, key_list):
        try:
            client = self.get_redis_instance()
            result = []
            if not key_list:
                key_list = client.keys("*")
            db_values = client.mget(key_list)
            for val in db_values:
                if val:
                    result.append(json.loads(val))
            return result
        except Exception as e:
            log_exception("Exception in TMXREPO: search | Cause: " + str(e), None, e)
            return None

    # Inserts the object into mongo collection
    def tmx_create(self, object_in):
        glossary = Glossary(
            source_language=object_in["sentences"][0]["locale"].split("|")[0],
            target_language=object_in["sentences"][0]["locale"].split("|")[1],
            source_text=object_in["sentences"][0]["src"],
            target_text=object_in["sentences"][0]["tgt"],
            user_id=User.objects.get(pk=int(object_in["userID"])),
        )
        glossary.save()

    # Searches tmx entries from mongo collection
    def search_tmx_db(self, user_id, org_id, locale):
        # col = self.instantiate_mongo_tmx()
        user, org = 0, 0
        if tmx_user_enabled:
            res_user = col.find({"locale": locale, "userID": user_id}, {"_id": False})
            if res_user:
                for record in res_user:
                    # log_info(f"Test68 USER TMX RECORDS: {record}",None)
                    user += 1
        if tmx_org_enabled:
            res_org = col.find({"locale": locale, "orgID": org_id}, {"_id": False})
            if res_org:
                for record in res_org:
                    org += 1

        if user > 0 and org > 0:
            return "BOTH"
        else:
            if user > 0:
                return "USER"
            elif org > 0:
                return "ORG"
        return None
