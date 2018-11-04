import unittest
from process_changes_with_object import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        self.assertEqual('Thomas', commits[0].author)
        self.assertEqual('Jimmy', commits[420].author)
        self.assertEqual('Vincent', commits[13].author)

        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
                'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
                commits[24].comment)
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                commits[20].changed_path)


    def test_other_columns(self):
        commits = get_commits(self.data)
        self.assertEqual('r1551925', commits[0].revision)
        self.assertEqual(1, commits[0].number_of_lines)
        self.assertEqual('16:57:44', commits[0].time)
        self.assertEqual('2015-11-27', commits[0].date)

if __name__ == '__main__':
    unittest.main()