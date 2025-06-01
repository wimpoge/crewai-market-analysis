from crewai import Agent, Crew, Process, Task
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() 

def save_results_to_file(result, filename_prefix="market_analysis"):
    """Save the crew analysis results to markdown format"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    md_filename = f"{filename_prefix}_{timestamp}.md"
    with open(md_filename, 'w', encoding='utf-8') as f:
        f.write("# CrewAI Market Analysis Report\n\n")
        f.write(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write("## Analysis Results\n\n")
        f.write(str(result))
        f.write("\n\n---\n\n")
        f.write("## Report Metadata\n\n")
        f.write("- **Agents Used:** Market Research Specialist, Market Analyst\n")
        f.write("- **Tasks Completed:** Market Research, Investment Analysis\n")
        f.write("- **Analysis Type:** AI Healthcare Market Analysis\n")
        f.write("\n---\n\n")
        f.write("*End of Report*\n")
    
    return md_filename

def main():
    print("Starting CrewAI Market Analysis...")
    
    researcher = Agent(
        role="Market Research Specialist",
        goal="Find comprehensive market data on emerging technologies",
        backstory="""You are an expert market researcher with 10+ years of experience 
        in technology markets. You excel at discovering market trends, gathering 
        accurate data, and identifying emerging opportunities in the tech sector.""",
        verbose=True,
        allow_delegation=False
    )
    
    analyst = Agent(
        role="Market Analyst",
        goal="Analyze market data and identify key opportunities",
        backstory="""You are a senior market analyst with expertise in investment 
        analysis and strategic planning. You excel at interpreting complex market 
        data, identifying patterns, and providing actionable investment recommendations.""",
        verbose=True,
        allow_delegation=False
    )
    
    research_task = Task(
        description="""Research the current market landscape for AI-powered healthcare solutions.
        Include:
        1. Market size and growth projections
        2. Key players and their market share
        3. Recent funding rounds and investments
        4. Regulatory landscape and challenges
        5. Emerging trends and technologies
        6. Geographic market breakdown""",
        expected_output="""Comprehensive market research report including:
        - Current market size (in USD)
        - 5-year growth projections
        - Top 10 key players with brief descriptions
        - Recent major investments and funding rounds
        - Key regulatory considerations
        - 3-5 emerging trends""",
        agent=researcher
    )
    
    analysis_task = Task(
        description="""Analyze the market research data and identify the top 3 investment 
        opportunities in AI-powered healthcare solutions. For each opportunity, provide:
        1. Investment rationale
        2. Market potential and size
        3. Risk assessment
        4. Competitive landscape
        5. Expected timeline for returns
        6. Recommended investment amount range""",
        expected_output="""Investment analysis report with:
        - Executive summary
        - Top 3 ranked investment opportunities
        - Detailed analysis for each opportunity including rationale, risks, and potential returns
        - Overall market outlook and recommendations
        - Risk mitigation strategies""",
        agent=analyst,
        context=[research_task]
    )
    
    market_analysis_crew = Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        process=Process.sequential,
        verbose=True,
        memory=True  # Enable memory for better context retention
    )
    
    try:
        print("Executing market analysis crew...")
        # Run the crew analysis
        result = market_analysis_crew.kickoff()
        
        print("\nAnalysis completed! Saving results to file...")
        
        # Save results to markdown file
        md_file = save_results_to_file(result)
        
        print(f"\nResults saved to: {md_file}")
        
        # Display a summary of the results
        print("\n" + "="*50)
        print("ANALYSIS SUMMARY")
        print("="*50)
        print(str(result)[:500] + "..." if len(str(result)) > 500 else str(result))
        
        return result
        
    except Exception as e:
        error_msg = f"Error during analysis: {str(e)}"
        print(error_msg)
        
        # Save error log
        error_filename = f"error_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(error_filename, 'w') as f:
            f.write(f"CrewAI Market Analysis Error\n")
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write(f"Error: {error_msg}\n")
        
        return None

if __name__ == "__main__":
    # API key is loaded from .env file via load_dotenv()
    if "OPENAI_API_KEY" not in os.environ:
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please ensure your .env file contains: OPENAI_API_KEY=your-api-key-here")
        exit(1)
    
    result = main()
    
    if result:
        print("\n✅ Market analysis completed successfully!")
        print("Check the generated files for detailed results.")
    else:
        print("\n❌ Market analysis failed. Check error log for details.")