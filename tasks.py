from crewai import Task

def get_tasks():
    return [
        Task(
            description="Retrieve relevant legal information for the user query: '{query}'",
            expected_output="Relevant legal context and document snippets",
            agent=None,  
        ),
        Task(
            description="Generate a detailed legal answer to the query: '{query}' based only on retrieved documents",
            expected_output="A complete, helpful response grounded in retrieved information",
            agent=None,
        ),
        Task(
            description="Evaluate the accuracy and completeness of the generated response for: '{query}'",
            expected_output="A brief report on the quality of the response",
            agent=None,
        ),
        Task(
            description="Polish and refine the response for clarity and professionalism for: '{query}'",
            expected_output="Final cleaned and concise answer",
            agent=None,
        ),
    ]