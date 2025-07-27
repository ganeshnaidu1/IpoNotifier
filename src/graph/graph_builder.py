from langgraph.graph import StateGraph, START, END
from src.nodes.prompt_generator import PromptGenerator
from src.tools.perplexity_tool import PerplexityTool
from src.state.state import state
from src.nodes.output_formatter import OutputFormatter
class GraphBuilder:
    def __init__(self, llm):
        self.graph_builder = StateGraph(state)
        self.llm = llm

    def build_graph(self):
        # Add nodes
        self.prompt_node = PromptGenerator()
        self.perplexity_tool = PerplexityTool(state)
        self.output_formatter = OutputFormatter(self.llm)
        self.graph_builder.add_node("prompt_generator",self.prompt_node.generate_prompt)
        self.graph_builder.add_node("perplexity_tool",self.perplexity_tool.get_open_ipos)
        self.graph_builder.add_node("output_formatter",self.output_formatter.format_output)
        self.graph_builder.add_edge(START, "prompt_generator")
        self.graph_builder.add_edge("prompt_generator", "perplexity_tool")
        self.graph_builder.add_edge("perplexity_tool", "output_formatter")
        self.graph_builder.add_edge("output_formatter", END)
        return self.graph_builder.compile()