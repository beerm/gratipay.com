from __future__ import print_function, unicode_literals

import mock
from aspen.http.request import UnicodeWithParams
from gittip import wireup
from gittip.elsewhere import twitter
from gittip.testing import Harness



class TestElsewhereTwitter(Harness):


    def setUp(self):
        wireup.elsewhere(self)


    def test_twitter_resolve_resolves(self):
        alice_on_twitter = twitter.TwitterAccount( "1"
                                                 , {'screen_name': 'alice'}
                                                  )
        alice_on_twitter.opt_in('alice')

        expected = 'alice'
        actual = twitter.resolve('alice')
        assert actual == expected


    @mock.patch('gittip.elsewhere.twitter.Twitter.hit_api')
    def test_can_load_account_elsewhere_from_twitter(self, hit_api):
        hit_api.return_value = {"id": "123", "screen_name": "alice"}

        alice_on_twitter = self.elsewhere.twitter.load(UnicodeWithParams('alice', {}))
        assert alice_on_twitter.user_id == "123"


    @mock.patch('gittip.elsewhere.twitter.Twitter.hit_api')
    def test_account_elsewhere_has_participant_object_on_it(self, hit_api):
        hit_api.return_value = {"id": "123", "screen_name": "alice"}
        alice_on_twitter = self.elsewhere.twitter.load(UnicodeWithParams('alice', {}))
        import pdb; pdb.set_trace()
        assert alice_on_twitter.participant.username == 'alice'
