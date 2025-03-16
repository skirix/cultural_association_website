# src/cultural_association_website/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM

@CrewBase
class CulturalAssociationWebsiteCrew():
    """Cultural Association Website development crew"""

    @agent
    def requirements_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['requirements_analyst'],
            verbose=True
        )

    @agent
    def ux_ui_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['ux_ui_designer'],
            verbose=True
        )

    @agent
    def frontend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_developer'],
            verbose=True
        )

    @agent
    def backend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_developer'],
            verbose=True
        )

    @agent
    def qa_tester(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_tester'],
            verbose=True
        )

    @task
    def requirements_gathering(self) -> Task:
        return Task(
            config=self.tasks_config['requirements_gathering'],
            output_file='output/requirements.md'
        )

    @task
    def design_creation(self) -> Task:
        return Task(
            config=self.tasks_config['design_creation'],
            output_file='output/design_spec.md'
        )

    @task
    def frontend_development(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_development'],
            output_file='output/frontend_code.md'
        )

    @task
    def backend_development(self) -> Task:
        return Task(
            config=self.tasks_config['backend_development'],
            output_file='output/backend_code.md'
        )

    @task
    def qa_testing(self) -> Task:
        return Task(
            config=self.tasks_config['qa_testing'],
            output_file='output/qa_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Cultural Association Website crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )