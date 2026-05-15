from duckduckgo_search import DDGS
import wikipedia
import arxiv

# DuckDuckGo Search
def search_web(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(f"{r['title']} - {r['href']}")
    return "\n".join(results)


# Wikipedia (robust version)
def get_wikipedia(query):
    try:
        if query.lower() in ["ai", "what is ai"]:
            query = "Artificial Intelligence"

        return wikipedia.summary(query, sentences=3)

    except wikipedia.exceptions.DisambiguationError as e:
        try:
            return wikipedia.summary(e.options[0], sentences=3)
        except:
            return "No Wikipedia result found."

    except:
        try:
            results = wikipedia.search(query)
            if results:
                return wikipedia.summary(results[0], sentences=3)
            else:
                return "No Wikipedia result found."
        except:
            return "No Wikipedia result found."


# arXiv
import time

def get_arxiv(query):
    try:
        search = arxiv.Search(
            query=query,
            max_results=3,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = []
        for paper in search.results():
            results.append(f"{paper.title} - {paper.entry_id}")
            time.sleep(1)  # prevent rate limit

        return "\n".join(results)

    except Exception as e:
        return "arXiv is currently rate-limited. Please try again later or refine your query."