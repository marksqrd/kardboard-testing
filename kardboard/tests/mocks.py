import datetime

from mock import Mock


class MockRemoteCustomFieldValue(object):
    def __init__(self, customfieldId, key, values):
        super(MockRemoteCustomFieldValue, self).__init__()
        self.customfieldId = customfieldId
        self.key = key
        self.values = values


class MockJIRAIssue(Mock):
    summary = "There's been a lot of lies in this family"
    key = "CMSAD-1"
    reporter = 'cheisel'
    assignee = 'cheisel'
    description = ''
    status = '6'
    type = '4'
    updated = datetime.datetime(2011, 12, 22, 12, 40, 19)

    customFieldValues = [
        MockRemoteCustomFieldValue(
            customfieldId='customfield_10210',
            key=None,
            values=['cheisel', ]
        ),
        MockRemoteCustomFieldValue(
            customfieldId='customfield_10211',
            key=None,
            values=['cheisel', ]
        ),
        MockRemoteCustomFieldValue(
            customfieldId='customfield_10133',
            key=None,
            values=['cheisel', ]
        ),
    ]


class MockJIRAObject(object):
    def __init__(self, dic):
        self.__dict__ = dic


class MockJIRAService(Mock):
    def getIssue(self, auth, key):
        return MockJIRAIssue()

    def login(self, user, password):
        return "Not much here"

    def getIssueTypes(self):
        return [
            MockJIRAObject({
                'description': '',
                'id': '4',
                'name': 'New Feature',
                'icon': \
                    'http://jira.example.com/images/icons/type_feature.gif',
            }),
        ]

    def getSubTaskIssueTypes(self):
        return [
            MockJIRAObject({
                'description': '',
                'id': '4',
                'name': 'Feature',
                'icon': \
                    'http://jira.example.com/images/icons/type_feature.gif',
            }),
        ]

    def getStatuses(self):
        return [MockJIRAObject({
            'description': '',
            'icon': 'http://jira.example.com/images/icons/status_closed.gif',
            'id': '6',
            'name': 'Closed',
        }), ]


class MockJIRAClient(Mock):
    service = MockJIRAService()
