from agent_candidate.agent_candidate import AgentCandidate


class TestAgentCandidate():
    def setup(self):
        self.candidate = AgentCandidate()

    def test_recommend_resume(self):
        self.candidate.recommend_resume()