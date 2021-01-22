from agent_candidate.agent_candidate import AgentCandidate


class TestAgentCandidate():
    def setup(self):
        self.candidate = AgentCandidate()

    def test_recommend_resume(self):
        self.candidate.recommend_resume()

    def test_check_has_resume(self):
        self.candidate.check_has_resume()

    def test_get_candidate_list(self):
        self.candidate.get_candidate_list()

    def test_get_resume_detail(self):
        self.candidate.get_resume_detail()

    def test_remind_stage_audit(self):
        self.candidate.remind_stage_audit()