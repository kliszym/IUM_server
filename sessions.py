import secrets


class Sessions:
    session = []

    @staticmethod
    def generate_id():
        return secrets.token_hex(32)

    @staticmethod
    def get_id(master):
        while True:
            user_id = Sessions.generate_id()
            if next((old_id for old_id in Sessions.session if old_id["user_id"] == user_id), None) is None:
                break
        Sessions.session.append({"user_id": user_id, "role": master})
        return user_id

    @staticmethod
    def verify_id(user_id):
        if next((old_id for old_id in Sessions.session if old_id["user_id"] == user_id), None) is None:
            return False
        return True

    @staticmethod
    def is_master(user_id):
        return next((old_id for old_id in Sessions.session if old_id["user_id"] == user_id), None)["role"]
