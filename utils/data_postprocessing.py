import re

def extract_and_clean_response(raw_output):
    """
    Extracts the relevant text from the raw output and cleans it up.
    
    Args:
        raw_output (str): The raw output from the agent.
        
    Returns:
        str: The cleaned and relevant text.
    """
    clean_output = re.sub(r"\x1b\[.*?m", "", raw_output)
    clean_output = re.sub(r"Running:\s*", "", clean_output)
    clean_output = re.sub(r"search_knowledge_base\(query=.*?\)", "", clean_output)
    match = re.search(r"Response.*?┃(.*?)┗", clean_output, re.DOTALL)
    if match:
        relevant_text = match.group(1).strip()
        relevant_text = re.sub(r"[\n\r]+", " ", relevant_text)  # Replace newlines with space
        relevant_text = re.sub(r"\s{2,}", " ", relevant_text)   # Replace multiple spaces with one
        relevant_text = relevant_text.replace("┃", "")          # Remove all occurrences of '┃'
        relevant_text = re.sub(r"•", "", relevant_text)         # Remove all occurrences of bullet points (•)
        relevant_text = re.sub(r"\s{2,}", " ", relevant_text)   # Replace multiple spaces with one
        return relevant_text
    return "No relevant content found"