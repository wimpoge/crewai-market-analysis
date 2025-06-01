# CrewAI Market Analysis

An AI-powered market research and analysis tool built with CrewAI that provides comprehensive insights into emerging technology markets, specifically focused on AI healthcare solutions.

## Features

- **Automated Market Research**: Comprehensive data gathering on market size, key players, funding, and trends
- **Investment Analysis**: Detailed analysis of top investment opportunities with risk assessments
- **Multi-Agent Collaboration**: Utilizes specialized agents for research and analysis tasks
- **Sequential Processing**: Ensures research data informs investment analysis
- **Error Handling**: Robust error logging and handling mechanisms

## Project Structure

```
├── app.py              # Main application file
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
├── .env                # Environment variables (not tracked)
└── requirements.txt    # Python dependencies
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd crewai-market-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## Usage

Run the market analysis:

```bash
python app.py
```

The application will:
1. Initialize two specialized AI agents (Market Research Specialist and Market Analyst)
2. Execute market research on AI-powered healthcare solutions
3. Perform investment analysis based on research findings
4. Display results summary in the console
5. Handle any errors with detailed logging

## Agents

### Market Research Specialist
- **Role**: Comprehensive market data discovery
- **Expertise**: Technology markets, trends, and emerging opportunities
- **Output**: Market size, growth projections, key players, funding data, regulatory landscape

### Market Analyst
- **Role**: Investment opportunity analysis
- **Expertise**: Investment analysis and strategic planning
- **Output**: Top 3 investment opportunities with detailed risk/return analysis

## Configuration

The application uses sequential processing to ensure the Market Analyst receives comprehensive research data before performing investment analysis. Memory is enabled for better context retention between tasks.

## Error Handling

- Comprehensive try-catch blocks for error management
- Detailed error logging with timestamps
- Graceful failure handling with informative messages

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for AI agent functionality | Yes |

## Output

The application provides:
- Console output with analysis progress and summary
- Error logs (if any issues occur)
- Detailed results display in terminal

## Dependencies

- `crewai` - Multi-agent AI framework
- `python-dotenv` - Environment variable management
- `datetime` - Timestamp functionality
- `os` - Operating system interface
