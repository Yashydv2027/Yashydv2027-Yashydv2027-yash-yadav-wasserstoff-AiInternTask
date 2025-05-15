
import arxiv
import os

def download_arxiv_papers(query="machine learning", max_results=75, save_dir="backend/data/arxiv_papers"):
    os.makedirs(save_dir, exist_ok=True)
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    for result in search.results():
        paper_path = os.path.join(save_dir, f"{result.get_short_id().replace('/', '_')}.pdf")
        if not os.path.exists(paper_path):
            result.download_pdf(filename=paper_path)
            print(f"Downloaded: {paper_path}")
        else:
            print(f"Already exists: {paper_path}")

if __name__ == "__main__":
    download_arxiv_papers()
