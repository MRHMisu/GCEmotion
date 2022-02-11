class CommitMessage:
    def __init__(self, encoded_message):
        self.encoded_message = encoded_message
        self.commit_title = ''
        self.commit_body = ''

    def get_commit_title(self):
        commit_title = self.to_string().splitlines()[0]
        return commit_title

    def get_commit_body(self):
        body_lines = self.to_string().splitlines()
        if len(body_lines) <= 1:
            return self.commit_body
        else:
            body_lines.pop(0)
            return '\n'.join(body_lines)

    def to_string(self):
        decoded_message = bytes.fromhex(self.encoded_message).decode('utf-8')
        return decoded_message
