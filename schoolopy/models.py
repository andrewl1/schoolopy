class _base_model(dict):
    def __init__(self, json):
        self.json = json
        self.update(json)
        self.update(self.__dict__)
        self.__dict__ = self

    def __repr__(self):
        contents = {k: self[k] for k in self if k != 'json'}  # Exclude :json: from the string
        return '%s(%s)' % (self.__class__.__name__, dict.__repr__(contents))


def _model(class_name):
    return type(class_name, (_base_model,), {})


class Message(_base_model):
    def __init__(self, json):
        super().__init__(json)
        self.recipient_ids = list(map(int, self.recipient_ids.split(',')))


class MessageThread(Message):
    pass


School = _model('School')
Building = _model('Building')
User = _model('User')
Enrollment = _model('Enrollment')
Group = _model('Group')
Course = _model('Course')
Section = _model('Section')
Event = _model('Event')
BlogPost = _model('BlogPost')
BlogPostComment = _model('BlogPostComment')
Discussion = _model('Discussion')
DiscussionReply = _model('DiscussionReply')
Update = _model('Update')
UpdateComment = _model('UpdateComment')
Reminder = _model('Reminder')
MediaAlbum = _model('MediaAlbum')
Media = _model('Media')
Document = _model('Document')
GradingScale = _model('GradingScale')
Rubric = _model('Rubric')
Assignment = _model('Assignment')
FriendRequest = _model('FriendRequest')
Invite = _model('Invite')
Grade = _model('Grade')
