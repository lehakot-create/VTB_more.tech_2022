import redis


class RedisConnector:
    conn = redis.StrictRedis(host='0.0.0.0',
                             decode_responses=True)

    def write_role(self, role):
        self.conn.rpush("roles", role)

    def get_all_roles(self):
        return self.conn.lrange("roles", 0, -1)

    def add_source(self, role, source: list):
        # print("source", source)
        for el in source:
            # print(el)
            # print(el.get('name'))
            self.conn.rpush(f"{role}_source", str({el.get("name"): el.get("url")}))

    def get_source(self, role):
        return self.conn.lrange(f"{role}_source", 0, -1)
